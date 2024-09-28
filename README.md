# ASISIA 
## BACKEND
___
### ESTRUCTURA
```text
my_project/
│
├── backend/
│   ├── manage.py
│   ├── config/
│   │   ├── settings.py
│   ├── core/
│   │   ├── models/
│   │   │   ├── user.py
│   │   │   ├── thesaurus.py
│   │   ├── views/
│   │   │   ├── auth_view.py
│   │   │   ├── thesaurus_view.py
│   │   ├── serializers/
│   │   │   ├── user_serializer.py
│   │   │   ├── thesaurus_serializer.py
│   │   ├── urls.py
│   └── db/
│       ├── thesaurus_db.json
│   └── logs/
│       ├── activity.log
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── index.jsx
│   │   ├── components/
│   │   │   ├── Login.jsx
│   │   │   ├── Dashboard.jsx
│   │   │   ├── ThesaurusForm.jsx
│   │   ├── context/
│   │   │   ├── AuthContext.jsx
│   │   │   ├── ThesaurusContext.jsx
│   │   ├── services/
│   │   │   ├── authService.js
│   │   │   ├── thesaurusService.js
│   ├── vite.config.js
│
└── README.md
```
### GIT
```text
echo "# asisia_be" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/zeron-team/asisia_be.git
git push -u origin master
```