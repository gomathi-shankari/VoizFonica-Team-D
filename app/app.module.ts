import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { PlansComponent } from './plans/plans.component';
import { AccountComponent } from './account/account.component';
import { ApiService } from './api.service';
import { NgImageSliderModule} from 'ng-image-slider';
import { SlickCarouselModule } from 'ngx-slick-carousel';
import { RechargeComponent } from './recharge/recharge.component';
import { FormsModule } from '@angular/forms';
import { ReactiveFormsModule } from '@angular/forms';
import { PrepaidComponent } from './prepaid/prepaid.component';
import { PostpaidComponent } from './postpaid/postpaid.component';
import { DongleComponent } from './dongle/dongle.component';
import { BuyingComponent } from './buying/buying.component';
import { FaqComponent } from './aichat/faq/faq.component';
import { BillComponent } from './aichat/bill/bill.component';
import { PlanComponent } from './aichat/plan/plan.component';
import { AichatModule } from './aichat/aichat.module';
import { TechnicalComponent } from './aichat/technical/technical.component';

@NgModule({
  declarations: [
    AppComponent,
    AccountComponent,
    RechargeComponent,
    PrepaidComponent,
    PostpaidComponent,
    DongleComponent,
    BuyingComponent,
    FaqComponent,
    BillComponent,
    TechnicalComponent,
    PlanComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    NgImageSliderModule,
    SlickCarouselModule,
    FormsModule,
    ReactiveFormsModule,
    AichatModule,
  ],
  providers: [ApiService],
  bootstrap: [AppComponent],
})
export class AppModule { }
