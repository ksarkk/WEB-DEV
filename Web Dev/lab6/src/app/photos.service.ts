import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Photo} from "./models";
import { Observable, of } from 'rxjs';

@Injectable({
  providedIn: 'root'
})

//Sending of requests
export class PhotoService {
  constructor(private client: HttpClient) {}

  getPhotos(): Observable<Photo[]>{
    return this.client.get<Photo[]>('https://jsonplaceholder.typicode.com/albums/1/photos');
  }

  getPhoto(id:number, title:string): Observable<Photo>{
      return this.client.get<Photo>(`https://jsonplaceholder.typicode.com/albums/1/photos/${id}`);
  }

}
