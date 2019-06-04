Aws cli
>>ssh -i “location to newkey.pem’ ec2-user@IP
>>aws --version
>>aws --configure
>>aws ec2 describe-regions
>>aws ec2 describe-regions  --output text
>>aws ec2 describe-regions  --output table

#Create new ia,m user
>>aws iam create-group mygroup
>>aws iam create-user --user-name myuser
>>aws iam add-user-to-group --user-name myuser --group-name mygroup
>>aws iam put-user-policy --user-name myuser --policy-name mypoweruserrole --policy-doocument file ://mypolicy.json
>>aws iam list-user-policies --user-name myuser
>>cat mypolicy.json
[
“version”:”2017-10-17”,
“statement” : [
 {
  “Effect”: “ allow”,
  “NotAction”:”iam:*”,
“Resource”:”*”
}
]
>>aws iam list-user-policies --user-name myuser
>>aws iam create-login-profile --user-name myuser --password 
>>aws iam create-access-key --user-name myuser

###Launch Ec2 instances

>>aws ec2 create-key-pair --key-name mynewkey --query “KeyMaterial” --output text >mynewkey1.pem
>>aws ec2 create-security-group --group-name MyGroup --description “My sec group”
>>aws ec2 authorize-security-group-ingress --group-name MyGroup --protocol tcp --port PORT --cidr IP/24
>>aws ec2 run-instances --image-id (from the page that list diff virtual machines ami-XYZ) --count 1 --instance-type t2.micro --key-name myNewKey --security-groups MyGroup
>>aws ec2  describe-instances --query ‘Reservation[*].Instances[*].[InstanceID, PublicIPAddress,State,Name]’ --output table

###Launch Ec2 instances //*****************NEW BUCKET  S3********************************************************

>>aws configure
>>aws s3 mb s3://cloud-USERID-bucket // NEWBUCKET
>>aws s3 cp “PATH_TO_LOCAL_FILE” “PATH_TO_FILE_WHERE_TOUPLOAD”
>>aws s3 cp “PATH_TO_LOCAL_FILE” “s3://cloud-USERID-bucket”
>>aws s3 cp s3://CLOUD-USERID-bucket/2956.jpg C:/users/archana_ch/









