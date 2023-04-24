# create s3 bucket
aws s3 mb s3://sam-code-marcos-hello

# Cloudformation package
aws cloudformation package --s3-bucket  sam-code-marcos-hello --template-file template.yaml --output-template-file \
    template-generated.yaml

aws cloudformation deploy --template-file template-generated.yaml --stack-name hello-world-sam --capabilities CAPABILITY_IAM