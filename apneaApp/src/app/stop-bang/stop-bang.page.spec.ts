import { CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { StopBangPage } from './stop-bang.page';

describe('StopBangPage', () => {
  let component: StopBangPage;
  let fixture: ComponentFixture<StopBangPage>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ StopBangPage ],
      schemas: [CUSTOM_ELEMENTS_SCHEMA],
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(StopBangPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
