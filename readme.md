simple web framework for Iron Forger

https://hackpad.com/Week-1-Make-a-Web-Framework-qJOpEzlYJZY

ideas:

* Web framework with has all content in the DB - codeless RESTful api
* maybe also a static site server
* Keep it very simple so it doesn't get boring
* Have an example app in mind the whole time to direct development

todo:

- [ ] script to dump some data in a DB
- [ ] Static content server
- [ ] templates and SQL queries for each RESTful operation - like Rails scaffolding, except you can't change it
    - [ ] index
    - [ ] show
    - [ ] new
    - [ ] edit
    - [ ] update
    - [ ] destroy
- [ ] Iron Forger example app (really script that puts data in a DB)
    * people
    * projects
    * ideas
    * weeks
- [ ] auth protecting the whole site - start with basic auth
- [ ] themes (Drupal-style) that are custumizable
- [ ] Make an example JS app that uses these routes

Later:

- [ ] views table - use a view to render html
- [ ] special users table - if a resource has an owner, only that owner can modify it
- [ ] admin mode - somebody can still edit everything
