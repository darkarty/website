To deploy on vagrant run:  

> vagrant destroy   
> vagrant up

and access localhost:8080 with incognito or private browser to prevent potential cache problems with other submissions

If you are running in CSIL, you may have to comment-in these lines in Vagrantfile:
>chef.channel = "stable"  
>chef.version = "12.10.24"
