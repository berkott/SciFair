import { CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { EpworthPage } from './epworth.page';

describe('EpworthPage', () => {
  let component: EpworthPage;
  let fixture: ComponentFixture<EpworthPage>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ EpworthPage ],
      schemas: [CUSTOM_ELEMENTS_SCHEMA],
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(EpworthPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
