一.环境配置
1.VSCode下载  安装python  chinese,path intellisence,npm,npm instellisence,Veture , Vue3,Snippets,vscode-icons,live-server插件
2.配置终端  切换到cmd
3.安装前端开发工具，小程序开发工具，git
4.创建远程仓库 myBlog
5.初始化本地仓库  git init
6.远程仓库和本地仓库进行关联 git remote add origin '你的远程仓库地址'
7.如果出现错误没有ssh 就创建密钥  ssh-keygen  查看生成的密钥 cat ~/.ssh/id_rsa.pub
8.推送四步骤
  git status 查看发生变化的文件
  git commit -m '备注'
  git push -u origin master 第一次提交
  git push 之后的提交
二、创建myBlog项目
1、空文件夹下执行创建django项目  django-admin startproject myBlog
2.给myBlog创建虚拟环境使用 python -m venv  env
3.进入到虚拟环境 .\\env\\Scripts\\activate
4.推出虚拟环境  deactivate 
5.使用VSCode打开myblog  执行 pythonmanage.py startproject myBlog

三、创建articles的models

1.创建model
2.在admin.py注册