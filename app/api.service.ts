import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable( { providedIn:'root' })
export class ApiService {
api_link:string='http://localhost:8000/';
constructor(private http: HttpClient) { }
getItems1() {
return this.http.get(this.api_link + 'api/list1/');
};
getItems2() {
return this.http.get(this.api_link + 'api/list2/');
};
getItems3() {
return this.http.get(this.api_link + 'api/list3/');
};
getItems4() {
return this.http.get(this.api_link + 'api/list4/');
};
getItems5() {
return this.http.get(this.api_link + 'api/list5/');
};
getItems6() {
return this.http.get(this.api_link + 'api/list6/');
};


}
