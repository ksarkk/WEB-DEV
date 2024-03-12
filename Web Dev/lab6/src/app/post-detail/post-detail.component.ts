import {Component, OnInit} from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import {POSTS} from "../fake-db";
import {Post, Photo, postList} from "../models";
import {PostService} from "../post.service";
import{ PhotoService } from "../photos.service";
import {Observable} from "rxjs";

@Component({
  selector: 'app-post-detail',
  templateUrl: './post-detail.component.html',
  styleUrls: ['./post-detail.component.css']
})
export class PostDetailComponent implements OnInit {
  post: Post;
  photo: Photo[];
  loaded: boolean;
  edittedPost: Post;



  constructor(private route: ActivatedRoute, private postService: PostService, private router: Router,
              private photoService:PhotoService) {
    this.post = {} as Post;
    this.photo = [];
    this.loaded = true;
    this.edittedPost = {} as Post;
  }

  ngOnInit() {

    // const id = Number(this.route.snapshot.paramMap.get('id'));    //gets an 'id' of the page URL
    // if(id){
    //   let num_id = +id;
    // }
    // this.getPhotos();

    this.route.paramMap.subscribe((params) => {
      const id = Number(params.get('id'));
      const title = String(params.get('title'));
      this.post = POSTS.find((album: Post) => album.id === id) as Post;

      //Find id from DataBase
      // this.post = POSTS.find((post:Post) =>post.id === id) as Post;

      //get the post details
      this.loaded = false;
      this.postService.getPost(id, title).subscribe((post: Post) => {
        this.post = post;
        if (!this.post.title) {
          this.post.title = title;
        }
        this.loaded = true;
      });
    });
  }

  // savePost() {
  //   this.postService.updatePost(this.post).subscribe((post: Post) => {
  //     this.post = post;
  //     const index = POSTS.findIndex(p => p.id === post.id);
  //     if (index !== -1) {
  //       POSTS[index].title = post.title;
  //     }
  //   });
  // }

  savePost() {
    for(let i of postList) {
      if(i.id === this.post.id) {
        i.title = this.edittedPost.title;
      }
    }
    this.post.title = this.edittedPost.title;
    this.edittedPost = {} as Post;
    this.loaded = false;
  }

  // this.postService.updatePost(this.post).subscribe((post: Post) => {
    //   const index = this.postService.getPosts().findIndex(p => p.id === post.id);
    //   if (index !== -1) {
    //     this.postService.posts[index] = post;
    //     this.post = post;
    //   }
    // });


  goBack() {
    this.router.navigate(['/posts']);
  }

  goToPhotos() {
    this.router.navigate(['/posts', this.post.id, 'photos']);
  }
}
