export interface Post{
  id: number;
  title: string;
  body: string;
}


export interface Photo{
  albumId: number;
  id: number;
  title: string;
  url: string;
  thumbnailUrl: string;
}

export const postList: Post[] = [];
export let numOfPosts = 100;
export function incrementNumOfAlbums() {
  numOfPosts += 1;
}
