from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from company_panel.models import Company


class Team:
    @staticmethod
    @login_required
    def team(request):
        company_id = request.user.company_id
        if Company.objects.filter(pk=company_id).exists():
            company = Company.objects.get(pk=company_id)
        else:
            company = 0
        return render(request, 'timesheets/company_panel/team.html', context={'company': company})

