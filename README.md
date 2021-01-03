一.环境配置
1.VSCode下载  安装python  chinese,path intellisence,npm,npm instellisence,Veture , Vue3,Snippets,vscode-icons,live-server插件
2.配置终端 默认shell 切换到cmd  选择command
3.安装前端开发工具hbuilder，微信小程序开发工具，git/github远程本地连接(注意：git进行环境配置)

二、创建远程仓库
1.创建远程仓库 myBlog
2.ssh-keygen 创建密钥  cat ~/.ssh/id_rsa.pub   查看生成的密钥
3.初始化本地仓库  git init
4.远程仓库和本地仓库进行关联 git remote add origin '你的远程ssh仓库地址' 
5.推送四步骤
  git status 查看发生变化的文件
  git add . 
  git commit -m '备注' 注明自己进行的每次动作
  git push -u origin master 第一次提交
  git push 之后的每次提交

三、创建myBlog项目
1、cmd命令提示符进入空文件夹下执行创建django项目  django-admin startproject myBlog
2.给myBlog创建虚拟环境使用 python -m venv  env  创建虚拟环境是python3中提供的venv    ***  python -m venv env 
3.进入到虚拟环境 激活虚拟环境 .\\env\\Scripts\\activate
4.退出当前虚拟环境  deactivate 
5.使用VSCode打开myblog  执行 python manage.py startapp app_name
6.在settings.py中进行注册每个app  INSTALLED_APPS  
7.创建models.py填写数据进行迁移数据库 写源编程类和str函数

四、创建articles的models
1.创建model及逆行数据库迁移
2.在admin.py注册每个app
3.对于文章管理员是有文章数据库中的所有相关字段
4.admin.site.register(Articles,ArticlesAdmin) 进行在admin管理员页面网址注册文章以及文章管理员 