# Make sure the Apt package lists are up to date, so we're downloading versions that exist.
cookbook_file "apt-sources.list" do
  path "/etc/apt/sources.list"
end
execute 'apt_update' do
  command 'apt-get update'
end

# Base configuration recipe in Chef.
package "wget"
package "ntp"
cookbook_file "ntp.conf" do
  path "/etc/ntp.conf"
end
execute 'ntp_restart' do
  command 'service ntp restart'
end

# other config 
package "python-dev"
package "python-pip"
package "nginx"

execute 'update_pip' do
	command 'pip install --upgrade pip'
end

execute 'install_flask' do
  command 'pip install flask'
end

execute 'install_gunicorn' do
	command 'pip install gunicorn'
end

cookbook_file "nginx-default" do
  path "/etc/nginx/sites-available/default"
end

execute 'nginx_restart' do
  command 'service nginx restart'
end

execute 'start_gunicorn' do
  command 'cd /home/ubuntu/project && gunicorn hello:app &'
end



