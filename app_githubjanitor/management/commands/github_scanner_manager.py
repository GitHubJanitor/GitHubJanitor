# django custom command (https://docs.djangoproject.com/en/1.11/howto/custom-management-commands/#module-django.core.management)
# - Should be the cmdline interface to the scanner.
# - Should support start/stop/status parameters

from django.core.management.base import BaseCommand, CommandError
from app_githubjanitor.models import TargetFile
from app_githubjanitor.models import GithubRepo
from github3 import login, GitHubStatus

class Command(BaseCommand):
    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument(
            'command', 
            nargs=1, 
            choices=['start', 'stop', 'status'],
            help='Init style commands to control the scanner service.'
        )

    def start_scan(self):
        '''
        Start the scanner. It should:
        1- scan for relevant repos
        2- search for offender files in those repos
        3- store in the database if offenders have been found
        '''
        self.stdout.write(self.style.SUCCESS('Successfully started the scanner service'))

    def stop_scan(self):
        '''Stop the scanning service. It will save the progress to be able to continue later.'''
        self.stdout.write(self.style.SUCCESS('Successfully stopped the scanner service'))

    def status(self):
        '''Print the status of the scanner'''
        self.stdout.write(self.style.SUCCESS('Successfully fetched the status of the scanner service'))

    def github_test(request):
        response = "<H1>This page will test the github user credentials</H1>"
    
        gh = login(settings.GITHUB_USERNAME, password=settings.GITHUB_TOKEN)
        GitHubJanitor = gh.user()
    
        response += "<p>User name: " + GitHubJanitor.name + "</p>"
        response += "<p>Login: " + GitHubJanitor.login + "</p>"
        response += "<p># Followers: " + str(GitHubJanitor.followers) + "</p>"
        response += "<p># ratelimit_remaining: " + str(GitHubJanitor.ratelimit_remaining) + "</p>"
    
        # count the forked repos for this user
        search_results = gh.search_repositories('user:' + settings.GITHUB_USERNAME + ' fork:only',
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
    
    def github_scanner(request):
        response = "<H1>This page will scan github for the repos we want, and will scan these repos to find the files we are looking for, if found it will add the repo name to the database.</H1>"
        # launch automatically and iterate until we are out of queries to avoid ban
        # The goal is to have a list of repos that can be scanned for target_files
        gh = login(settings.GITHUB_USERNAME, password=settings.GITHUB_TOKEN)
        GitHubJanitor = gh.user()
    
        # buscar
        # gh.search_repositories(query, sort=None, order=None, per_page=None, text_match=False, number=-1, etag=None)
        response += "<p># ratelimit_remaining: " + str(GitHubJanitor.ratelimit_remaining) + "</p>"
    
        ##################
        # 1. Find all the repos that are not a fork, have been modified after a given date and have at least X stars
        search_results_repos = gh.search_repositories('pushed:>2017-09-17+fork:false+stars:>10',
                                                sort=None,
                                                order=None,
                                                per_page=None,
                                                text_match=False,
                                                number=-1,
                                                etag=None)
    
       
        return HttpResponse(response)

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Successfully parsed parameters, running functions.'))
        if options['command'] == 'start':
            self.start_scan()
        elif options['command'] == 'stop':
            self.stop_scan()
        elif options['command'] == 'status':
            self.status()

