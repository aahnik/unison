from django.shortcuts import render
from django.http import Http404
from django.contrib.auth.decorators import permission_required
from .models import Transanction, ExpenseCategory, BillerDetails, Direction
from .forms import GetStatementForm

from django.db.models import Sum


# Create your views here.
@permission_required("accounts.view_transanction", login_url="/admin/login")
def get_statement(request):
    ctx = {}
    if request.method == "POST":
        form = GetStatementForm(request.POST)
        if form.is_valid():
            print("valid")
            category = form.cleaned_data["account_category"]
            start_date = form.cleaned_data["start_date"]
            end_date = form.cleaned_data["end_date"]
            queryset = Transanction.objects.filter(
                category=category, tdate__range=[start_date, end_date]
            )
            # category = ExpenseCategory.objects.get()
            expense = queryset.filter(ttype=Direction.EXPENSE).aggregate(Sum("amount"))[
                "amount__sum"
            ]
            income = queryset.filter(ttype=Direction.INCOME).aggregate(Sum("amount"))[
                "amount__sum"
            ]
            cat_bal = ExpenseCategory.objects.get(category=category)

            ctx.update(
                {
                    "queryset": queryset,
                    "income": income,
                    "expense": expense,
                    "cat_bal": cat_bal.category_balance,
                    "num_txn": len(queryset),
                }
            )

            # print(form)
            # Process the form data here
            # For example, save the data to the database or perform other actions
            pass
    else:
        form = GetStatementForm()

    ctx.update({"form": form})
    return render(request, "accounts/statement.html", ctx)


@permission_required("accounts.view_transanction", login_url="/admin/login")
def view_invoice(request):
    invoice_id = request.GET["id"]
    try:
        transaction = Transanction.objects.get(auto_invoice_id=invoice_id)
        biller = BillerDetails.get_solo()
        return render(
            request,
            "accounts/invoice.html",
            {"transanction": transaction, "biller": biller},
        )
    except Transanction.DoesNotExist as err:
        raise Http404("Invoice does not exist.")
