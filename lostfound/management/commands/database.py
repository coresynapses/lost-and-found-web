# Database.py

# Common Python Imports
import os
import sys
import csv
import re

# Django-Specific Imports
import django
from django.core.management.base import BaseCommand

# Project-Specific Imports
from lostfound.models import *


# Functions
def loadItemsCsv():
    print("\nConfiguring items:")
    with open("data/items.csv") as f:
        reader = csv.reader(f)
        is_first = True
        for row in reader:
            if is_first:
                is_first = False
                continue
            primary_key = int(row[3])
            print(f"Primary key: {primary_key}")
            category = Category.objects.get(pk = primary_key)


            if len(row[5]) == 0:
                row[5] = "1990-01-01"

            item = Item(
                pk               = row[0],
                itemName         = row[1],
                description      = row[2],
                category         = category,
                dateReported     = row[4],
                dateClaimed      = row[5],
                location         = row[6],
                photo            = row[7],
                status           = row[8],
                disposition      = row[9],
                contactInfo      = row[10],
                proofOfOwnership = row[11],
            )
            item.save()

def loadCategoriesCsv():
    print("\nConfiguring categories:")
    with open("data/categories.csv") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
            category = Category(
                # categoryId   = row[0],
                categoryName = row[1],
            )
            category.save()

def loadClaimRequestReportsCsv():
    print("\nConfiguring claim request reports:")
    with open("data/claim_request_reports.csv") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

def loadFraudClaimReportsCsv():
    print("\nConfiguring fraud claim reports:")
    with open("data/fraud_claim_reports.csv") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

def loadUsersCsv():
    print("\nConfiguring users:")
    with open("data/users.csv") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

def setupDatabase():
    clearDatabase
    loadCategoriesCsv()
    loadUsersCsv()
    loadItemsCsv()
    loadClaimRequestReportsCsv()
    loadFraudClaimReportsCsv()

def showDatabase():
    print("Showing categories:")
    categories = Category.objects.all()
    for category in categories:
        print(f"- Key: {category.pk}; Name: {category.categoryName}")

def clearDatabase():
    print("Clearing database")

# Command
class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("--mode", nargs=1, type=int)

    def handle(self, *args, **options):
        match options["mode"][0]:
            case 0: # Setup
                setupDatabase()
            case 1: # Clear
                clearDatabase()
            case 2: # Show Database Contents
                showDatabase()
        
