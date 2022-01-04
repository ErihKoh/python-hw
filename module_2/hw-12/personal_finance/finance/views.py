from datetime import datetime

from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView
from django.http import HttpResponseRedirect, HttpResponse
from django.utils.text import slugify
import json
from .models import Project, Category, Expense
from .forms import ExpenseForm, FilterForm


def project_list(request):
    project_list = Project.objects.all()
      
    if request.method == 'DELETE':
        id = json.loads(request.body)['id']
       
        project = get_object_or_404(Project, id=id)
        project.delete()
        return HttpResponse('')

    return render(request, 'finance/project-list.html', {'project_list': project_list})


def project_detail(request, project_slug):
    project = get_object_or_404(Project, slug=project_slug)

    print(project)

    form1 = FilterForm(request.POST)
    form = ExpenseForm(request.POST)

    if request.method == 'POST':

        if form.is_valid():
                
                title = form.cleaned_data['title']
                amount = form.cleaned_data['amount']
                dateExpense = form.cleaned_data['dateExpense']
                category_name = form.cleaned_data['category']

                category = get_object_or_404(Category, project=project, name=category_name)

                Expense.objects.create(
                    project=project,
                    title=title,
                    amount=amount,
                    dateExpense=dateExpense,
                    category=category
                ).save()
            
        if form1.is_valid():
            start = form1.cleaned_data['start']
            end = form1.cleaned_data['end']
            print(type(start), end)
        


    elif request.method == 'GET':
        category_list = Category.objects.filter(project=project)
        return render(request, 'finance/project-detail.html',
                      {'project': project, 'expense_list': project.expenses.all(),
                       'category_list': category_list})

    elif request.method == 'DELETE':
        id = json.loads(request.body)['id']
        expense = get_object_or_404(Expense, id=id)
        expense.delete()
        return HttpResponse('')

    return HttpResponseRedirect(project_slug)


class ProjectCreateView(CreateView):
    model = Project
    template_name = 'finance/add-project.html'
    fields = ('name', 'budget')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()

        categories = self.request.POST['categoriesString'].split(',')
        for category in categories:
            Category.objects.create(
                project=Project.objects.get(id=self.object.id),
                name=category
            ).save()

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return slugify(self.request.POST['name'])
