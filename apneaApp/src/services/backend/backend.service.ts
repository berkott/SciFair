import { Injectable } from '@angular/core';

const {
  Stitch,
  RemoteMongoClient,
  UserPasswordCredential
} = require('mongodb-stitch-browser-sdk');


@Injectable({
  providedIn: 'root'
})

export class BackendService {
  private client = Stitch.initializeDefaultAppClient('brainappsnitch-qsgqh')

  constructor() { }

  async login(username: string, password: string){
    const credential = new UserPasswordCredential(username, password);

    return this.client.auth.loginWithCredential(credential);
  }

  async logout(){
    this.client.auth.logout();
  }

  async pushMuseData(_username: string, _password: string){
    const mongodb = this.client.getServiceClient(RemoteMongoClient.factory,"mongodb-atlas");

    return mongodb.db("general").collection('museData').insertOne({
      userid: this.client.auth.user.id,
      username: _username,
      password: _password
    }); 
  }

  async checkQuests(){
    let ep = true;
    let bang = true;

    await this.checkEpworth().then(val => {
      console.log("entered");

      if(val.length == 0){
        ep = false;
      }
    });
      
    await this.checkStopBang().then(val => {
      console.log("entered");

      if(val.length == 0){
        bang = false;
      }
    });

    if(ep == true && bang == true){
      return true;
    }
    return false;
  }

  async checkEpworth(){
    const mongodb = this.client.getServiceClient(RemoteMongoClient.factory,"mongodb-atlas");

    return mongodb.db("Epworth").collection('answers').find({userid: this.client.auth.user.id}).toArray();    
  }

  async checkStopBang(){
    const mongodb = this.client.getServiceClient(RemoteMongoClient.factory,"mongodb-atlas");

    return mongodb.db("stopBang").collection('answers').find({userid: this.client.auth.user.id}).toArray();
  }

  async sendAnswers(database: string, answers: number[]){
    const mongodb = this.client.getServiceClient(RemoteMongoClient.factory,"mongodb-atlas");
    
    await console.log(this.client.auth.user.id);

    return mongodb.db(database).collection('answers').insertOne({
      userid: this.client.auth.user.id,
      ans1: answers[0],
      ans2: answers[1],
      ans3: answers[2],
      ans4: answers[3],
      ans5: answers[4],
      ans6: answers[5],
      ans7: answers[6],
      ans8: answers[7]
    }); 
  }

  async sendPostAnswers(answers: any[]){
    const mongodb = this.client.getServiceClient(RemoteMongoClient.factory,"mongodb-atlas");
    
    await console.log(this.client.auth.user.id);

    return mongodb.db("postSleep").collection('answers').insertOne({
      userid: this.client.auth.user.id,
      ans1: answers[0],
      ans2: answers[1],
      ans3: answers[2],
      ans4: answers[3],
      ans5: answers[4],
      ans6: answers[5],
      ans7: answers[6],
      ans71: answers[7],
      ans8: answers[8],
      ans9: answers[9],
      ans91: answers[10],
      ans10: answers[11],
      ans11: answers[12]
    }); 
  }

  async getMainData(){
    const mongodb = this.client.getServiceClient(RemoteMongoClient.factory,"mongodb-atlas");

    return mongodb.db("general").collection('score')
      .find({userid: this.client.auth.user.id}).toArray();
  }
}
