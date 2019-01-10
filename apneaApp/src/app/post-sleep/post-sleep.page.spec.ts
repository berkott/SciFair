import { CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { PostSleepPage } from './post-sleep.page';

describe('PostSleepPage', () => {
  let component: PostSleepPage;
  let fixture: ComponentFixture<PostSleepPage>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ PostSleepPage ],
      schemas: [CUSTOM_ELEMENTS_SCHEMA],
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(PostSleepPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
