import {Component, OnInit} from '@angular/core';
import {Vacancy} from "../models";
import {CompaniesService} from "../companies.service";
import {ActivatedRoute} from "@angular/router";

@Component({
  selector: 'app-vacancies',
  templateUrl: './vacancies.component.html',
  styleUrls: ['./vacancies.component.css']
})
export class VacanciesComponent implements OnInit {
  vacancies: Vacancy[] = [];

  constructor(private companyService: CompaniesService, private route: ActivatedRoute) {
  }

  ngOnInit(): void {
    const routeParams = this.route.snapshot.paramMap;

    const comId = Number(routeParams.get('companyId'));
    this.companyService.getVacancies(comId).subscribe(
      (vacancies: Vacancy[]) => this.vacancies = vacancies);
  }

}
