# CODSOFT
CodSoft Internship 

devops lab 
trigger:
- main

pool:
  vmImage: 'ubuntu-latest'

stages:

- stage: Build
  displayName: 'Build Stage'
  jobs:
  - job: BuildJob
    steps:
    - script: echo "Building project..."
      displayName: 'Build'

- stage: Test
  displayName: 'Test Stage'
  dependsOn: Build
  jobs:
  - job: TestJob
    steps:
    - script: echo "Running tests..."
      displayName: 'Test'
