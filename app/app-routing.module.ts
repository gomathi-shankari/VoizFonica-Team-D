import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { PlansComponent} from './plans/plans.component';
import { AccountComponent} from './account/account.component';
import { RechargeComponent} from './recharge/recharge.component';
import { PrepaidComponent} from './prepaid/prepaid.component';
import { PostpaidComponent} from './postpaid/postpaid.component';
import { DongleComponent} from './dongle/dongle.component';
import { BuyingComponent} from './buying/buying.component';
import { FaqComponent } from './aichat/faq/faq.component';
import { BillComponent } from './aichat/bill/bill.component';
import { PlanComponent } from './aichat/plan/plan.component';
import { AichatModule } from './aichat/aichat.module';
import { TechnicalComponent } from './aichat/technical/technical.component';

const routes: Routes = [
{path:'plans',
component: PlansComponent},
{path:'account',
component: AccountComponent},
{path:'recharge',
component: RechargeComponent},
{path:'prepaid',
component: PrepaidComponent},
{path:'postpaid',
component: PostpaidComponent},
{path:'dongle',
component: DongleComponent},
{path:'buying',
component: BuyingComponent},
{path:'faq',
component: FaqComponent},
{path:'bill',
component: BillComponent},
{path:'plan',
component: PlanComponent},
{path:'technical',
component: TechnicalComponent},
]

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }



