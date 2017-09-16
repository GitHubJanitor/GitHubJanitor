# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("<H1>Turn this page into a dashboard</H1>")

def status(request):
    return HttpResponse("<H1>Put a global status page here</H1>")

def github_test(request):
    response = "<H1>This page will test the github user credentials</H1>"

    from github3 import login, GitHubStatus

    gh = login(GITHUB_USERNAME, password=GITHUB_TOKEN)

    GitHubJanitor = gh.user()

    response += "<p>User name: " + GitHubJanitor.name + "</p>"
    response += "<p>Login: " + GitHubJanitor.login + "</p>"
    response += "<p># Followers: " + str(GitHubJanitor.followers) + "</p>"
    response += "<p># ratelimit_remaining: " + str(GitHubJanitor.ratelimit_remaining) + "</p>"

    # count the forked repos
    search_results = gh.search_repositories('user:' + GITHUB_USERNAME + ' fork:only',
                                            sort=None,
                                            order=None,
                                            per_page=None,
                                            text_match=False,
                                            number=-1,
                                            etag=None)

    repos_forked = sum(1 for _ in search_results)
    response += "<p># Current repos forked: " + str(repos_forked) + "</p>"

    #######################
    gh_status = GitHubStatus()
    response += "<p>GitHub Status: " + str(gh_status.status()) + "</p>"
    #######################

    return HttpResponse(response)

    # buscar
    # gh.search_repositories(query, sort=None, order=None, per_page=None, text_match=False, number=-1, etag=None)
