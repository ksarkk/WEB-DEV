import {Component, OnInit} from '@angular/core';
import {Post, postList} from "../models";
import {PostService} from "../post.service";
import {Observable} from "rxjs";
import {POSTS} from "../fake-db";

@Component({
  selector: 'app-posts',
  templateUrl: './posts.component.html',
  styleUrls: ['./posts.component.css']
})
export class PostsComponent implements OnInit{
  posts: Post[];
  newPost: Post;
  loaded: boolean;
  constructor(private postService:PostService) {
    this.posts = [];
    this.loaded = true;
    this.newPost = {} as Post;
  }

  ngOnInit() {
    // this.posts = POSTS;
    //Read the data from another resources
    this.getPosts();
  }

  // getPosts(){
  //   this.loaded = false;
  //   this.postService.getPosts().subscribe((posts: Post[]) => {
  //     this.posts = posts;
  //     this.loaded = true;
  //   });
  // }

  getPosts() {
    if(postList.length != 0) {
      this.posts = postList;
    } else {
      this.postService.getPosts().subscribe((posts) => {
        this.posts= posts;
        for(let i of posts) {
          postList.push(i);
        }
      });
    }
  }
  addPost(){
    this.postService.addPost(this.newPost).subscribe((post:Post)=>{
      if(post.title == null){
        alert("You didn't enter any posts");
      }
      else{
        const newPost: Post = {
          id: this.posts.length + 1,
          title: post.title,
          body: post.body,
        };
        this.posts.unshift(newPost);
        this.loaded = true;
        this.newPost = {} as Post;
      }
    });
  }

  deletePost(id: number) {
    this.postService.deletePost(id).subscribe(() => {
      this.posts = this.posts.filter(post => post.id !== id);
    });
  }


}
