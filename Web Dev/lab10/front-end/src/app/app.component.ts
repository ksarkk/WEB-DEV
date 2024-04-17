import {Component, OnInit} from '@angular/core';
import {Company} from "./models";
import {CompaniesService} from "./companies.service";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit{
  title = 'hh-front';

  companies: Company[] = [];
  newCompany: string = " ";

  constructor(private companyService: CompaniesService) {
  }

  ngOnInit(){
    this.companyService.getCompanies().subscribe((data:Company[])=>{
      this.companies = data;
    })
  }

  addCompany(){
    console.log(this.newCompany);
  }
}
