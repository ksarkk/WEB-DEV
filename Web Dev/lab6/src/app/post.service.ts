import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Post, postList} from "./models";
import { Observable, of } from 'rxjs';

@Injectable({
  providedIn: 'root'
})

//Sending of requests
export class PostService {
    BASE_URL: string = 'https://jsonplaceholder.typicode.com';
  constructor(private client: HttpClient) {

  }

  getPosts(): Observable<Post[]>{
    return this.client.get<Post[]>('https://jsonplaceholder.typicode.com/posts');
  }

  // getPost(id:number, title:string): Observable<Post>{
  //   if (id<=100) {
  //     return this.client.get<Post>(`https://jsonplaceholder.typicode.com/posts/${id}`);
  //   }
  //   else{
  //     return of({
  //       id: id,
  //       title: title,
  //       body: 'new body'
  //     })
  //   }
  // }

  getPost(id: number, title:string): Observable<Post> {
    if(id > 100) {
      const album =  postList.find(p => p.id === id);
      if(album) {
        return of(album)
      }
    }
    return this.client.get<Post>(`https://jsonplaceholder.typicode.com/posts/${id}`);
  }

  addPost(post: Post): Observable<Post>{
    return this.client.post<Post>('https://jsonplaceholder.typicode.com/posts', post);
  }

  deletePost(id: number): Observable<void> {
    return this.client.delete<void>(`https://jsonplaceholder.typicode.com/posts/${id}`);
  }

  updatePost(post: Post): Observable<Post> {
    return this.client.put<Post>(
      `https://jsonplaceholder.typicode.com/posts/${post.id}`,
      post
    );
  }

  // updatePost(post: Post): Observable<Post> {
  //   const url = 'https://jsonplaceholder.typicode.com/posts/${post.id}';
  //   // const headers = new HttpHeaders().set('Content-Type', 'application/json; charset=UTF-8');
  //   const body = JSON.stringify(post);
  //
  //   return this.client.put<Post>(url, body);
  // }

}
