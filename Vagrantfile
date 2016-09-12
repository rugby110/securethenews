# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.network "forwarded_port", guest: 8000, host: 8000
  config.vm.define "securethenews" do |securethenews|
    securethenews.vm.hostname = "securethenews"
    securethenews.vm.provision "ansible" do |ansible|
      ansible.playbook = "ansible/playbook.yml"
    end
    securethenews.vm.provider "virtualbox" do |vb|
      # Building nodejs packages triggers the OOM killer with 512MB of RAM.
      vb.memory = 1024
    end
  end
end
