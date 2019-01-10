# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Python imports
from datetime import date, timedelta


# Django imports
from django.views.generic import View as V
from django.db.models import Min


# Project imports
from cricket.models import Match


class View(V):
    '''
        A generic view for the matches section
    '''

    context = {}

    def get_seasons(self):
        # start_year = int(
        #     PlayCricketTeam.objects.filter(
        #         match_results=True,
        #         active=True,
        #     ).aggregate(
        #         Min('first_season')
        #     )['first_season__min']
        # )
        start_year = 2018
        return range(date.today().year, start_year - 1, -1)

    def get_date(self):
        return date.today()

    def get_results(self, **kwargs):
        return Match.objects.filter(
            **kwargs
        ).order_by(
            '-date__date'
        )

    def get_fixtures(self):
        today = self.get_date()
        one_week = today + timedelta(days=7)
        return Match.objects.filter(
            date__date__range=[today, one_week]
        ).order_by(
            'date__date'
        )

    # Context managers
    def clear_context(self):
        self.context = {}

    def add_context(self, key, value):
        if key not in self.context.keys():
            self.context[key] = value
        else:
            raise KeyError('Key already set in context')

    def update_context(self, key, value):
        if key not in self.context.keys():
            raise KeyError('Key not set in context')
        else:
            self.context[key] = value

    def get_context(self):
        return self.context


