import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {HomeComponent} from "./home/home.component";
import {AboutComponent} from "./about/about.component";
import {NotFoundComponent} from "./not-found/not-found.component";
import {PostsComponent} from "./posts/posts.component";
import {PostDetailComponent} from "./post-detail/post-detail.component";
import {AlbumPhotosComponent} from "./album-photos/album-photos.component";

const routes: Routes = [
  {path: 'home', component: HomeComponent},    //if path contains 'home', render HomeComponent
  {path: 'about', component: AboutComponent},
  {path:'posts', component: PostsComponent},
  {path:'posts/:id', component: PostDetailComponent},
  {path:'posts/:id/photos', component: AlbumPhotosComponent},
  {path: '', redirectTo:'home', pathMatch:'full'},
  {path: '**', component: NotFoundComponent},  //if no matching, render NotFoundComponent
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
