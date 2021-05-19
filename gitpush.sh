git init
git add .
git status

git commit -m 'automatico'
git push
git config credential.helper store        
git config --global credential.helper store
git config credential.helper cache
git config --global credential.helper cache

git status
