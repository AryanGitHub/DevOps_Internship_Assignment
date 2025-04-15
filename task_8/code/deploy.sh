#!/bin/bash
aws cloudformation deploy --region ap-south-1 \
    --template-file ./main.yaml \
    --stack-name ecsaimodel \
    --tags madeFromCLI=yeah anotherTagForAllStackResources=okay \
    --capabilities CAPABILITY_NAMED_IAM
    #--no-execute-changeset