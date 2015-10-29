"""
@apiDefine cloudhost 云主机API
"""

"""
@api {get} cloud_servers        云主机列表
@apiGroup cloudhost
@apiExample {curl} 示例:
            curl -i -X GET http://api.speedycloud.cn/api/v1/products/cloud_servers
            -H "Accept: application/json"
            -H "Content-Type: application/json; charset=utf-8"
            -H "API-KEY: a6bea3f8e0a1ef8d26a3bd0a7a8f491ddca0989a68a8dc2a5adb82e3a0fd6ca9"
            -H "API-REQUEST-DATE: Thu, 02 Apr 2015 02:45:18 GMT"
            -H "API-HMAC: 447dcb5f6fdb7d8dd344a76d9cc4a72593689976"
@apiName cloudhostList
@apiVersion 1.0.0
@apiDescription                 获取客户云主机列表

@apiParam None                 　无

@apiSuccess {Number} id         云主机ID
@apiSuccess {String} name       云主机的名称
@apiSuccess {String} alias 云主机的别名
@apiSuccess {String} group_name 云主机所属的组名
@apiSuccess {String} status 云主机的状态:Created, Provisioning, Running, Stopped, Suspended
@apiSuccess {String} tags 云主机的标签信息
@apiSuccess {String} cpu 云主机的ＣＰＵ数量
@apiSuccess {String} memory 云主机的内存大小
@apiSuccess {String} disk 云主机的磁盘大小
@apiSuccess {String} ips 云主机的ＩＰ地址
@apiSuccessExample {Array} 返回数据
    返回值类型: Array
    Array中包含的是云主机基本信息的JSON Hash:
[
    {
        "status": "Running",
        "disk": 40,
        "name": "i-jzgoiesw",
        "tags": "",
        "has_running_job": true,
        "created_at": "2014-08-07 10:47:48",
        "availability_zone": {
            "display_name": "北京数据中心;Beijing-01",
            "name": "SPC-BJ-1"
        },
        "cpu": 2,
        "group_name": "",
        "ips": [],
        "bandwidth": 12,
        "alias": "",
        "memory": 2,
        "id": 28,
        "disk_type": "Normal",
        "image": "Ubuntu 12.04",
        "network": {
            "display_name": "中国电信",
            "name": "China Telecom"
        },
        "monitor_url": "/api/status?name=i-jzgoiesw"
    }
]
"""

"""
@api {get} cloud_servers/:id　            云主机信息
@apiName cloudhostInfo
@apiGroup cloudhost
@apiExample {curl} 示例:
    URL中的:id为云主机的ID
    curl -i -X GET http://api.speedycloud.cn/api/v1/products/cloud_servers/28
    -H "Accept: application/json"
    -H "Content-Type: application/json; charset=utf-8"
    -H "API-KEY: a6bea3f8e0a1ef8d26a3bd0a7a8f491ddca0989a68a8dc2a5adb82e3a0fd6ca9"
    -H "API-REQUEST-DATE: Thu, 02 Apr 2015 02:45:18 GMT"
    -H "API-HMAC: 447dcb5f6fdb7d8dd344a76d9cc4a72593689976"
@apiVersion 1.0.0
@apiDescription                          获取客户云主机详细信息

@apiParam {Number}  id id为云主机的ID

@apiSuccess {Number} id 云主机ID
@apiSuccess {String} name               云主机的名称
@apiSuccess {String} alias              云主机的别名
@apiSuccess {String} group_name         云主机所属的组名
@apiSuccess {String} hostname           云主机的主机名
@apiSuccess {String} status             云主机的状态:Created, Provisioning, Running, Stopped, Suspended
@apiSuccess {String} tags               云主机的标签信息
@apiSuccess {String} cpu                云主机的ＣＰＵ数量
@apiSuccess {String} memory             云主机的内存大小
@apiSuccess {String} disk               云主机的磁盘大小
@apiSuccess {String} ips                云主机的ＩＰ地址
@apiSuccess {String} availability_zone  云主机所在的Availability Zone
@apiSuccess {String} image          云主机的磁盘镜像模板名称
@apiSuccess {String} network            云主机的网络供应商名称
@apiSuccess {String} uptime 	        云主机的运行时间，单位为小时
@apiSuccess {String} bootscript 	云主机的启动脚本
@apiSuccess {String} backup_quota 	云主机的备份配额
@apiSuccess {String} backup_usage 	云主机的备份使用量
@apiSuccess {String} default_password 	云主机的默认root密码
@apiSuccess {String} monitoring_url 	云主机的监控数据URL
@apiSuccess {String} created_at 	云主机的创建日期
@apiSuccessExample {Array}  返回数据:
    返回值类型: Hash
    内容为云主机的详细信息:
{
    "availability_zone": {
        "display_name": "北京数据中心;Beijing-01",
        "name": "SPC-BJ-1"
    },
    "image": "Ubuntu 12.04",
    "group_name": "",
    "ips": [],
    "bandwidth": "12Mbps",
    "disk": "40GB",
    "id": 28,
    "security_groups": [],
    "monitor_url": "/api/status?name=i-jzgoiesw",
    "network": {
        "display_name": "中国电信",
        "name": "China Telecom"
    },
    "disable_private_network": false,
    "hostname": "i-jzgoiesw",
    "bootscript": "",
    "memory": "2048MB",
    "metadata": "",
    "status": "Running",
    "joined_networks": [],
    "tags": "",
    "disk_type": "Normal",
    "has_running_job": true,
    "name": "i-jzgoiesw",
    "created_at": "2014-08-07 10:47:48",
    "alias": "",
    "volumes": [],
    "default_password": "1234567",
    "cpu": "2"
}

"""
"""
@api {get}  cloud_servers/:id/backups　云主机备份列表
@apiName cloudhostBackupsList
@apiGroup cloudhost
@apiExample {curl} 示例:
    URL中的:id为云主机的ID
    curl -i -X GET http://api.speedycloud.cn/api/v1/products/cloud_servers/28/backup
    -H "Accept: application/json"
    -H "Content-Type: application/json; charset=utf-8"
    -H "API-KEY: a6bea3f8e0a1ef8d26a3bd0a7a8f491ddca0989a68a8dc2a5adb82e3a0fd6ca9"
    -H "API-REQUEST-DATE: Thu, 02 Apr 2015 02:45:18 GMT"
    -H "API-HMAC: 447dcb5f6fdb7d8dd344a76d9cc4a72593689976"
@apiVersion 1.0.0
@apiDescription 获取客户单台云主机的备份列表。

@apiParam {Number}  id id为云主机的ID

@apiSuccess {String} name 备份的名称
@apiSuccess {String} date　备份的日期
@apiSuccess {String} status 备份的状态:waiting, running, success
@apiSuccess {String} size 备份的大小
@apiSuccessExample {Array} 返回数据:
    返回值类型: Array
    Array中的元素为备份信息的Hash:
[
    {
        "status": "waiting",
        "date": "2015-09-11 17:23:06",
        "name": "asd",
        "size": 0
    }
]

"""

"""
@api {get}  cloud_servers/:id/jobs　         云主机任务列表
@apiName cloudhostTaskList
@apiGroup cloudhost
@apiExample {curl} 示例:
    URL中的:id为云主机的ID
    curl -i -X GET http://api.speedycloud.cn/api/v1/products/cloud_servers/28/jobs
    -H "Accept: application/json"
    -H "Content-Type: application/json; charset=utf-8"
    -H "API-KEY: a6bea3f8e0a1ef8d26a3bd0a7a8f491ddca0989a68a8dc2a5adb82e3a0fd6ca9"
    -H "API-REQUEST-DATE: Thu, 02 Apr 2015 02:45:18 GMT"
    -H "API-HMAC: 447dcb5f6fdb7d8dd344a76d9cc4a72593689976"
@apiVersion 1.0.0
@apiDescription         获取客户单台云主机的任务列表。

@apiParam {Number}  id id为云主机的ID

@apiSuccess {Number} id 任务的ID
@apiSuccess {String} name　任务的名称
@apiSuccess {String} server 云主机的名称
@apiSuccess {String} status 任务的状态: queue, running, success, fail
@apiSuccess {String} finished   任务是否完成
@apiSuccess {String} created_at     任务创建时间
@apiSuccess {String} finished_at 任务完成时间
@apiSuccessExample {Array}  返回数据:
    返回值类型: Array
    Array中的元素为任务信息的Hash:
[
    {
        "status": "queue",
        "name": "provision",
        "created_at": "2014-08-07 10:47:48",
        "server": "i-jzgoiesw",
        "finished": false,
        "id": 45
    },
    {
        "status": "queue",
        "name": "stop",
        "created_at": "2014-08-14 15:39:01",
        "server": "i-jzgoiesw",
        "finished": false,
        "id": 47
    },
    {
        "status": "queue",
        "name": "resize",
        "created_at": "2015-09-02 12:39:40",
        "server": "i-jzgoiesw",
        "finished": false,
        "id": 49
    },
    {
        "status": "queue",
        "name": "backup",
        "created_at": "2015-09-11 17:23:06",
        "server": "i-jzgoiesw",
        "finished": false,
        "id": 50
    }
]
"""

"""
@api {post}  cloud_servers/:id/start　启动云主机
@apiName cloudhostStart
@apiGroup  cloudhost
@apiExample {curl} 示例:
    URL中的:id为云主机的ID
    curl -i -X POST http://api.speedycloud.cn/api/v1/products/cloud_servers/28/start
    -H "Accept: application/json"
    -H "Content-Type: application/json; charset=utf-8"
    -H "API-KEY: a6bea3f8e0a1ef8d26a3bd0a7a8f491ddca0989a68a8dc2a5adb82e3a0fd6ca9"
    -H "API-REQUEST-DATE: Thu, 02 Apr 2015 02:45:18 GMT"
    -H "API-HMAC: 447dcb5f6fdb7d8dd344a76d9cc4a72593689976"
    -d '{"id":28}'
@apiVersion 1.0.0
@apiDescription  启动指定的云主机，只有当云主机处于关闭（Stopped）状态时有效。

@apiParam {Number}  id id为云主机的ID

@apiSuccess {Number} id     任务的ID
@apiSuccess {String} name   任务的名称
@apiSuccess {String} server     云主机的名称
@apiSuccess {String} status     任务的状态: queue, running, success,fail
@apiSuccess {String} finished   任务是否完成
@apiSuccess {String} created_at     任务创建时间
@apiSuccess {String} finished_at    任务完成时间
@apiSuccessExample {Array} 返回数据:
    返回值类型: Hash
    返回内容为任务的详细信息, Hash中Key的说明信息:
{
    "status": "queue",
    "name": "start",
    "created_at": "2015-09-11 18:49:48",
    "server": "i-jzgoiesw",
    "finished": false,
    "id": 53
}
"""

"""
@api {post}  cloud_servers/:id/restart  重启云主机
@apiExample {curl} 示例:
    URL中的:id为云主机的ID
    curl -i -X POST http://api.speedycloud.cn/api/v1/products/cloud_servers/28/restart
    -H "Accept: application/json"
    -H "Content-Type: application/json; charset=utf-8"
    -H "API-KEY: a6bea3f8e0a1ef8d26a3bd0a7a8f491ddca0989a68a8dc2a5adb82e3a0fd6ca9"
    -H "API-REQUEST-DATE: Thu, 02 Apr 2015 02:45:18 GMT"
    -H "API-HMAC: 447dcb5f6fdb7d8dd344a76d9cc4a72593689976"
@apiName cloudhostRestart
@apiGroup  cloudhost
@apiVersion 1.0.0
@apiDescription  重启指定的云主机，云主机在运行（Running）或者关闭（Stopped）的状态时有效。

@apiParam {Number}  id URL中的:id为云主机的ID

@apiSuccess {Number} id     任务的ID
@apiSuccess {String} name   任务的名称
@apiSuccess {String} server     云主机的名称
@apiSuccess {String} status     任务的状态: queue, running, success, fail
@apiSuccess {String} finished   任务是否完成
@apiSuccess {String} created_at     任务创建时间
@apiSuccess {String} finished_at    任务完成时间
@apiSuccessExample {Array} 返回值类型: Hash
    返回内容为任务的详细信息, Hash中Key的说明信息:
{
    "status": "queue",
    "name": "restart",
    "created_at": "2015-09-11 18:49:48",
    "server": "i-jzgoiesw",
    "finished": false,
    "id": 53
}

"""

"""
@api {post}  cloud_servers/:id/stop  关闭云主机
@apiName cloudhostClose
@apiGroup  cloudhost
@apiExample {curl} 示例:
    URL中的:id为云主机的ID
    curl -i -X POST http://api.speedycloud.cn/api/v1/products/cloud_servers/28/stop
    -H "Accept: application/json"
    -H "Content-Type: application/json; charset=utf-8"
    -H "API-KEY: a6bea3f8e0a1ef8d26a3bd0a7a8f491ddca0989a68a8dc2a5adb82e3a0fd6ca9"
    -H "API-REQUEST-DATE: Thu, 02 Apr 2015 02:45:18 GMT"
    -H "API-HMAC: 447dcb5f6fdb7d8dd344a76d9cc4a72593689976"
    -d '{"id":28}'
@apiVersion 1.0.0
@apiDescription 关闭指定的云主机，云主机处于运行（Running）和挂起（Suspended）状态时有效。

@apiParam {Number}  id id为云主机的ID

@apiSuccess {Number} id     任务的ID
@apiSuccess {String} name   任务的名称
@apiSuccess {String} server     云主机的名称
@apiSuccess {String} status     任务的状态: queue, running, success, fail
@apiSuccess {String} finished   任务是否完成
@apiSuccess {String} created_at     任务创建时间
@apiSuccess {String} finished_at    任务完成时间
@apiSuccessExample {Array} 返回数据:
    返回值类型: Hash
    返回内容为任务的详细信息, Hash中Key的说明信息:

{
    "status": "queue",
    "name": "stop",
    "created_at": "2015-09-11 18:41:22",
    "server": "i-jzgoiesw",
    "finished": false,
    "id": 52
}

"""

"""
@api {post}  cloud_servers/:id/suspend 　挂起云主机
@apiName cloudhostHangup
@apiGroup  cloudhost
@apiExample {curl} 示例:
    URL中的:id为云主机的ID
    curl -i -X POST http://api.speedycloud.cn/api/v1/products/cloud_servers/28/suspend
    -H "Accept: application/json"
    -H "Content-Type: application/json; charset=utf-8"
    -H "API-KEY: a6bea3f8e0a1ef8d26a3bd0a7a8f491ddca0989a68a8dc2a5adb82e3a0fd6ca9"
    -H "API-REQUEST-DATE: Thu, 02 Apr 2015 02:45:18 GMT"
    -H "API-HMAC: 447dcb5f6fdb7d8dd344a76d9cc4a72593689976"
    -d '{"id":28}'
@apiVersion 1.0.0
@apiDescription 挂起指定的云主机，只有云主机在运行（Running）的状态时有效。

@apiParam {Number}  id URL中的:id为云主机的ID
@apiSuccess {Number} id     任务的ID

@apiSuccess {String} name   任务的名称
@apiSuccess {String} server     云主机的名称
@apiSuccess {String} status     任务的状态: queue, running, success, fail
@apiSuccess {String} finished   任务是否完成
@apiSuccess {String} created_at     任务创建时间
@apiSuccess {String} finished_at    任务完成时间
@apiSuccessExample {Array} 返回数据:
    返回值类型: Hash
    返回内容为任务的详细信息, Hash中Key的说明信息:
{
    "status": "queue",
    "name": "suspend",
    "created_at": "2015-09-11 18:49:48",
    "server": "i-jzgoiesw",
    "finished": false,
    "id": 53
}
"""

"""
@api {post} cloud_servers/:id/resume　　恢复云主机
@apiName cloudhostRecover
@apiGroup  cloudhost
@apiExample {curl} 示例:
    URL中的:id为云主机的ID
    curl -i -X POST http://api.speedycloud.cn/api/v1/products/cloud_servers/28/resume
    -H "Accept: application/json"
    -H "Content-Type: application/json; charset=utf-8"
    -H "API-KEY: a6bea3f8e0a1ef8d26a3bd0a7a8f491ddca0989a68a8dc2a5adb82e3a0fd6ca9"
    -H "API-REQUEST-DATE: Thu, 02 Apr 2015 02:45:18 GMT"
    -H "API-HMAC: 447dcb5f6fdb7d8dd344a76d9cc4a72593689976"
    -d '{"id":28}'
@apiVersion 1.0.0
@apiDescription 恢复指定挂起中的云主机，只有在云主机处于挂起（Suspended）状态时有效。

@apiParam {Number}  id id为云主机的ID

@apiSuccess {Number} id     任务的ID
@apiSuccess {String} name   任务的名称
@apiSuccess {String} server     云主机的名称
@apiSuccess {String} status     任务的状态: queue, running, success, fail
@apiSuccess {String} finished   任务是否完成
@apiSuccess {String} created_at     任务创建时间
@apiSuccess {String} finished_at    任务完成时间
@apiSuccessExample {Array} 返回数据:
    返回值类型: Hash
    返回内容为任务的详细信息, Hash中Key的说明信息:
{
    "status": "queue",
    "name": "resume",
    "created_at": "2015-09-11 18:49:48",
    "server": "i-jzgoiesw",
    "finished": false,
    "id": 53
}
"""

"""
@api {post}  cloud_servers/:id/backup　　备份云主机
@apiName cloudhostBackups
@apiGroup cloudhost
@apiExample {curl} 示例:
    URL中的:id为云主机的ID
    curl -i -X POST http://api.speedycloud.cn/api/v1/products/cloud_servers/28/backup
    -H "Accept: application/json"
    -H "Content-Type: application/json; charset=utf-8"
    -H "API-KEY: a6bea3f8e0a1ef8d26a3bd0a7a8f491ddca0989a68a8dc2a5adb82e3a0fd6ca9"
    -H "API-REQUEST-DATE: Thu, 02 Apr 2015 02:45:18 GMT"
    -H "API-HMAC: 447dcb5f6fdb7d8dd344a76d9cc4a72593689976"
    -d '{"id":28,"name":"name"}'
@apiVersion 1.0.0
@apiDescription  为指定云主机创建备份。

@apiParam {Number}  id id为云主机的ID
@apiParam {String}  name QueryString中的参数: name 备份的名称

@apiSuccess {Number} id     任务的ID
@apiSuccess {String} name   任务的名称
@apiSuccess {String} server     云主机的名称
@apiSuccess {String} status     任务的状态: queue, running, success, fail
@apiSuccess {String} finished   任务是否完成
@apiSuccess {String} created_at     任务创建时间
@apiSuccess {String} finished_at    任务完成时间
@apiSuccessExample {Array} 返回数据:
    返回值类型: Hash
    返回内容为任务的详细信息, Hash中Key的说明信息:
{
  "status": "queue",
  "name": "backup",
  "created_at": "2015-09-13 12:35:44",
  "server": "i-jzgoiesw",
  "finished": false,
  "id": 56
}
"""

"""
@api {post} cloud_servers/:id/backups/:name/restore　　恢复云主机备份
@apiName cloudhostRecoverbackups
@apiGroup  cloudhost
@apiExample {json} 示例:
    URL中的:id为云主机的ID
    curl -i -X POST http://api.speedycloud.cn/api/v1/products/cloud_servers/28/backups/text_backup/restore
    -H "Accept: application/json"
    -H "Content-Type: application/json; charset=utf-8"
    -H "API-KEY: a6bea3f8e0a1ef8d26a3bd0a7a8f491ddca0989a68a8dc2a5adb82e3a0fd6ca9"
    -H "API-REQUEST-DATE: Thu, 02 Apr 2015 02:45:18 GMT"
    -H "API-HMAC: 447dcb5f6fdb7d8dd344a76d9cc4a72593689976"
    -d '{"id":28,"name":"name"}'
@apiVersion 1.0.0
@apiDescription URL中的:为云主机恢复指定的备份。

@apiParam {Number}  id id为云主机的ID
@apiParam {String}  name QueryString中的参数: name 备份的名称

@apiSuccess {Number} id     任务的ID
@apiSuccess {String} name   任务的名称
@apiSuccess {String} server     云主机的名称
@apiSuccess {String} status     任务的状态: queue, running, success, fail
@apiSuccess {String} finished   任务是否完成
@apiSuccess {String} created_at     任务创建时间
@apiSuccess {String} finished_at    任务完成时间
@apiSuccessExample {Array} 返回数据:
    返回值类型: Hash
    返回内容为任务的详细信息, Hash中Key的说明信息:
{
  "status": "queue",
  "name": "restorebackup",
  "created_at": "2015-09-13 12:35:44",
  "server": "i-jzgoiesw",
  "finished": false,
  "id": 56
}
"""

"""
@api {post}     cloud_servers/:id/backups/:name/delete　　删除云主机备份
@apiName cloudhostBackupsDelete
@apiGroup cloudhost
@apiExample {json} 示例:
    URL中的:id为云主机的ID
    curl -i -X POST http://api.speedycloud.cn/api/v1/products/cloud_servers/28/backups/text_backup/delete
    -H "Accept: application/json"
    -H "Content-Type: application/json; charset=utf-8"
    -H "API-KEY: a6bea3f8e0a1ef8d26a3bd0a7a8f491ddca0989a68a8dc2a5adb82e3a0fd6ca9"
    -H "API-REQUEST-DATE: Thu, 02 Apr 2015 02:45:18 GMT"
    -H "API-HMAC: 447dcb5f6fdb7d8dd344a76d9cc4a72593689976"
    -d '{"id":28,"name":"name"}'
@apiVersion 1.0.0
@apiDescription 为云主机恢复指定的备份。

@apiParam {Number}  id id为云主机的ID
@apiParam {String}  name 备份的名称

@apiSuccess {Number} id     任务的ID
@apiSuccess {String} name   任务的名称
@apiSuccess {String} server     云主机的名称
@apiSuccess {String} status     任务的状态: queue, running, success, fail
@apiSuccess {String} finished   任务是否完成
@apiSuccess {String} created_at     任务创建时间
@apiSuccess {String} finished_at    任务完成时间
@apiSuccessExample {Array} 返回数据:
    返回值类型: Hash
    返回内容为任务的详细信息, Hash中Key的说明信息:
{
  "status": "queue",
  "name": "restorebackup",
  "created_at": "2015-09-13 12:35:44",
  "server": "i-jzgoiesw",
  "finished": false,
  "id": 56
}
"""

"""
@api {post}     cloud_servers/:id/tag　 为云主机设置标签
@apiExample {json} 示例:
    URL中的:id为云主机的ID
    curl -i -X POST http://api.speedycloud.cn/api/v1/products/cloud_servers/28/backups/text_backup/delete
    -H "Accept: application/json"
    -H "Content-Type: application/json; charset=utf-8"
    -H "API-KEY: a6bea3f8e0a1ef8d26a3bd0a7a8f491ddca0989a68a8dc2a5adb82e3a0fd6ca9"
    -H "API-REQUEST-DATE: Thu, 02 Apr 2015 02:45:18 GMT"
    -H "API-HMAC: 447dcb5f6fdb7d8dd344a76d9cc4a72593689976"
    -d '{"id":28,"tag":"tag_name"}'

@apiName cloudhostSetTag
@apiGroup cloudhost
@apiVersion 1.0.0
@apiDescription 为指定云主机设置标签。

@apiParam {Number}  id URL中的:id为云主机的ID
@apiParam {String}  tag QueryString中的参数: tag 标签的内容

@apiSuccess {Number} id     任务的ID
@apiSuccess {String} name   任务的名称
@apiSuccess {String} server     云主机的名称
@apiSuccess {String} status     任务的状态: queue, running, success, fail
@apiSuccess {String} finished   任务是否完成
@apiSuccess {String} created_at     任务创建时间
@apiSuccess {String} finished_at    任务完成时间
@apiSuccessExample {Array} 返回数据:
    返回值类型: Hash
    返回内容为任务的详细信息, Hash中Key的说明信息:
    {
        "availability_zone": "北京数据中心;Beijing-01",
        "image": "Ubuntu 12.04",
        "ips": [],
        "bandwidth": "12Mbps",
        "disk": "40GB",
        "id": 28,
        "security_groups": [],
        "monitor_url": "/api/status?name=i-jzgoiesw",
        "cluster_name": "",
        "uptime": 0,
        "network": "中国电信",
        "disable_private_network": false,
        "backup_usage": 0,
        "hostname": "i-jzgoiesw",
        "cpu_mode": "host-passthrough",
        "bootscript": "",
        "memory": "2048MB",
        "metadata": "",
        "status": "Running",
        "joined_networks": [],
        "tags": "tag",
        "backup_quota": 100,
        "has_running_job": true,
        "name": "i-jzgoiesw",
        "created_at": "2014-08-07 10:47:48",
        "volumes": [],
        "default_password": "1234567",
        "cpu": "2"
    }
"""

"""
@api {post}     cloud_servers/:id/alias　为云主机设置别名
@apiName cloudhostAlias
@apiGroup  cloudhost
@apiExample {curl} 示例:
    URL中的:id为云主机的ID
    curl -i -X POST http://api.speedycloud.cn/api/v1/products/cloud_servers/28/backup
    -H "Accept: application/json"
    -H "Content-Type: application/json; charset=utf-8"
    -H "API-KEY: a6bea3f8e0a1ef8d26a3bd0a7a8f491ddca0989a68a8dc2a5adb82e3a0fd6ca9"
    -H "API-REQUEST-DATE: Thu, 02 Apr 2015 02:45:18 GMT"
    -H "API-HMAC: 447dcb5f6fdb7d8dd344a76d9cc4a72593689976"
    -d '{"id":28,"alias":"alias_name"}'
@apiVersion 1.0.0
@apiDescription 为指定云主机设置别名。

@apiParam {Number}  id id为云主机的ID
@apiParam {String}  alias QueryString中的参数: alias 标签的内容

@apiSuccess {Number} id     云主机的ID
@apiSuccess {String} name   云主机的名称
@apiSuccess {String} alias  云主机的别名
@apiSuccess {String} group_name     云主机所属的组名
@apiSuccess {String} hostname   云主机的主机名
@apiSuccess {String} status     云主机的状态: Created, Provisioning, Running, Stopped, Suspended
@apiSuccess {String} tags   云主机的标签信息
@apiSuccess {String} cpu    云主机的CPU数量
@apiSuccess {String} memory     云主机的内存大小
@apiSuccess {String} disk   云主机的磁盘大小
@apiSuccess {String} ips    云主机的IP地址
@apiSuccess {String} availability_zone  云主机所在的Availability Zone
@apiSuccess {String} image  云主机的磁盘镜像模板名称
@apiSuccess {String} network    云主机的网络供应商名称
@apiSuccess {String} uptime     云主机的运行时间，单位为小时
@apiSuccess {String} bootscript     云主机的启动脚本
@apiSuccess {String} backup_quota   云主机的备份配额
@apiSuccess {String} backup_usage   云主机的备份使用量
@apiSuccess {String} default_password   云主机的默认root密码
@apiSuccess {String} monitoring_url     云主机的监控数据URL
@apiSuccess {String} created_at     云主机的创建日期
@apiSuccessExample {Array} 返回数据:
返回值类型: Hash
内容为云主机的详细信息:
{
    "availability_zone": "北京数据中心;Beijing-01",
    "image": "Ubuntu 12.04",
    "ips": [],
    "bandwidth": "12Mbps",
    "disk": "40GB",
    "id": 28,
    "security_groups": [],
    "monitor_url": "/api/status?name=i-jzgoiesw",
    "cluster_name": "",
    "uptime": 0,
    "network": "中国电信",
    "disable_private_network": false,
    "backup_usage": 0,
    "hostname": "i-jzgoiesw",
    "cpu_mode": "host-passthrough",
    "bootscript": "",
    "memory": "2048MB",
    "metadata": "",
    "status": "Running",
    "joined_networks": [],
    "tags": "tag",
    "backup_quota": 100,
    "has_running_job": true,
    "name": "i-jzgoiesw",
    "created_at": "2014-08-07 10:47:48",
    "volumes": [],
    "default_password": "1234567",
    "cpu": "2"
}
"""

"""
@api {post} cloud_servers/:id/group 为云主机设置分组
@apiExample {curl} 示例:
    URL中的:id为云主机的ID
    curl -i -X POST http://api.speedycloud.cn/api/v1/products/cloud_servers/28/backup
    -H "Accept: application/json"
    -H "Content-Type: application/json; charset=utf-8"
    -H "API-KEY: a6bea3f8e0a1ef8d26a3bd0a7a8f491ddca0989a68a8dc2a5adb82e3a0fd6ca9"
    -H "API-REQUEST-DATE: Thu, 02 Apr 2015 02:45:18 GMT"
    -H "API-HMAC: 447dcb5f6fdb7d8dd344a76d9cc4a72593689976"
    -d '{"id":28,"group":"group_name"}'
@apiName cloudhostSetGroup
@apiGroup  cloudhost
@apiVersion 1.0.0
@apiDescription 为指定云主机设置分组。

@apiParam {Number}  id id为云主机的ID
@apiParam {String}  group  QueryString中的参数: group  分组名称

@apiSuccess {Number} id     云主机的ID
@apiSuccess {String} name   云主机的名称
@apiSuccess {String} alias  云主机的别名
@apiSuccess {String} group_name     云主机所属的组名
@apiSuccess {String} hostname   云主机的主机名
@apiSuccess {String} status     云主机的状态: Created, Provisioning, Running, Stopped, Suspended
@apiSuccess {String} tags   云主机的标签信息
@apiSuccess {String} cpu    云主机的CPU数量
@apiSuccess {String} memory     云主机的内存大小
@apiSuccess {String} disk   云主机的磁盘大小
@apiSuccess {String} ips    云主机的IP地址
@apiSuccess {String} availability_zone  云主机所在的Availability Zone
@apiSuccess {String} image  云主机的磁盘镜像模板名称
@apiSuccess {String} network    云主机的网络供应商名称
@apiSuccess {String} uptime     云主机的运行时间，单位为小时
@apiSuccess {String} bootscript     云主机的启动脚本
@apiSuccess {String} backup_quota   云主机的备份配额
@apiSuccess {String} backup_usage   云主机的备份使用量
@apiSuccess {String} default_password   云主机的默认root密码
@apiSuccess {String} monitoring_url     云主机的监控数据URL
@apiSuccess {String} created_at     云主机的创建日期
@apiSuccessExample {Array}  返回数据:
返回值类型: Hash
内容为云主机的详细信息:
{
    "availability_zone": "北京数据中心;Beijing-01",
    "image": "Ubuntu 12.04",
    "ips": [],
    "bandwidth": "12Mbps",
    "disk": "40GB",
    "id": 28,
    "security_groups": [],
    "monitor_url": "/api/status?name=i-jzgoiesw",
    "cluster_name": "",
    "uptime": 0,
    "network": "中国电信",
    "disable_private_network": false,
    "backup_usage": 0,
    "hostname": "i-jzgoiesw",
    "cpu_mode": "host-passthrough",
    "bootscript": "",
    "memory": "2048MB",
    "metadata": "",
    "status": "Running",
    "joined_networks": [],
    "tags": "tag",
    "backup_quota": 100,
    "has_running_job": true,
    "name": "i-jzgoiesw",
    "created_at": "2014-08-07 10:47:48",
    "volumes": [],
    "default_password": "1234567",
    "cpu": "2"
}
"""

"""
@api {post}  cloud_servers/:id/change_image　变更操作系统
@apiName cloudhostChangeSystem
@apiGroup cloudhost
@apiExample {curl} 示例:
    URL中的:id为云主机的ID
    curl -i -X POST http://api.speedycloud.cn/api/v1/products/cloud_servers/id/backup
    -H "Accept: application/json"
    -H "Content-Type: application/json; charset=utf-8"
    -H "API-KEY: a6bea3f8e0a1ef8d26a3bd0a7a8f491ddca0989a68a8dc2a5adb82e3a0fd6ca9"
    -H "API-REQUEST-DATE: Thu, 02 Apr 2015 02:45:18 GMT"
    -H "API-HMAC: 447dcb5f6fdb7d8dd344a76d9cc4a72593689976"
    -d '{"id":28,"image":"Ubuntu 12.04"}'
@apiVersion 1.0.0
@apiDescription 修改云主机的操作系统。该操作只能在云主机处于运行(Running)或者关闭(Stopped)时执行，
并且在执行过程中云主机会处于关闭状态。如果您的操作系统是Linux则无法替换成Windows系统，
如果您的操作系统是Windows同样也无法替换成Linux。
如果要替换的操作系统模板与当前云主机运行的操作系统模板相同，
则等同于把系统盘恢复到初始状态。<br /><br />
<code style="font-size:15px">注意：当执行修改云主机操作系统时会删除系统盘中的数据，如果您有数据保留在系统盘中，请确认您的数据备份到数据盘或者其他云主机上。</code>

@apiParam {Number}  id id为云主机的ID
@apiParam {String}  image  操作系统模板名称

@apiSuccess {Number} id     任务的ID
@apiSuccess {String} name   任务的名称
@apiSuccess {String} server     云主机的名称
@apiSuccess {String} status     任务的状态: queue, running, success, fail
@apiSuccess {String} finished   任务是否完成
@apiSuccess {String} created_at     任务创建时间
@apiSuccess {String} finished_at    任务完成时间
@apiSuccessExample {Array} 返回数据:
    返回值类型: Hash
    返回内容为任务的详细信息, Hash中Key的说明信息:
{
  "status": "queue",
  "name": "restoretemplate",
  "created_at": "2015-09-14 12:36:47",
  "server": "i-jzgoiesw",
  "finished": false,
  "id": 58
}
"""

"""
@api {post}   cloud_servers/:id/attach/:volume_name　挂载云硬盘
@apiExample {curl} 示例:
    URL中的:id为云主机的ID
    curl -i -X POST http://api.speedycloud.cn/api/v1/products/cloud_servers/21/attach/v-xohrqfed
    -H "Accept: application/json"
    -H "Content-Type: application/json; charset=utf-8"
    -H "API-KEY: a6bea3f8e0a1ef8d26a3bd0a7a8f491ddca0989a68a8dc2a5adb82e3a0fd6ca9"
    -H "API-REQUEST-DATE: Thu, 02 Apr 2015 02:45:18 GMT"
    -H "API-HMAC: 447dcb5f6fdb7d8dd344a76d9cc4a72593689976"
    -d '{"id":28,"volume_name":"volume_name"}'
@apiName cloudhostMountCloudDrive
@apiGroup   cloudhost
@apiVersion 1.0.0
@apiDescription URL中的:为云主机挂载云硬盘。
注意： 云主机和云硬盘要在同一个数据中心才可以进行挂载。如果您想让云主机能在线增加云硬盘，在Linux操作系统中需要运行以下命令：modprobe acpiphp 如果您在挂载云硬盘前没运行上述命令，那么可以先卸载云硬盘等运行上面命令之后再进行挂载即可。

@apiParam {Number}  id id为云主机的ID
@apiParam {String}  name　云硬盘名称。（例如: i-testvolume）

@apiSuccess {Number} id     任务的ID
@apiSuccess {String} name   任务的名称
@apiSuccess {String} server     云主机的名称
@apiSuccess {String} status     任务的状态: queue, running, success, fail
@apiSuccess {String} finished   任务是否完成
@apiSuccess {String} created_at     任务创建时间
@apiSuccess {String} finished_at    任务完成时间
@apiSuccessExample {Array} 返回数据:
返回值类型: Hash
返回内容为任务的详细信息, Hash中Key的说明信息:
{
  "status": "queue",
  "name": "restoretemplate",
  "created_at": "2015-09-14 12:36:47",
  "server": "i-jzgoiesw",
  "finished": false,
  "id": 58
}
"""

"""
@api {post}    cloud_servers/:id/detach/:volume_name　卸载云硬盘
@apiExample {curl} 示例:
    URL中的:id为云主机的ID
    curl -i -X POST http://api.speedycloud.cn/api/v1/products/cloud_servers/21/detach/v-xohrqfed
    -H "Accept: application/json"
    -H "Content-Type: application/json; charset=utf-8"
    -H "API-KEY: a6bea3f8e0a1ef8d26a3bd0a7a8f491ddca0989a68a8dc2a5adb82e3a0fd6ca9"
    -H "API-REQUEST-DATE: Thu, 02 Apr 2015 02:45:18 GMT"
    -H "API-HMAC: 447dcb5f6fdb7d8dd344a76d9cc4a72593689976"
    -d '{"id":28,"volume_name":"volume_name"}'
@apiName cloudhostdetachCloudDrive
@apiGroup   cloudhost
@apiVersion 1.0.0
@apiDescription URL中的:为云主机卸载已经挂载的云硬盘。
注意： 在卸载云硬盘前请确保您的云主机已经停止使用云硬盘中的数据（Linux系统中已经umount对应的分区），否则这种非正常操作可能会导致数据损坏。

@apiParam {Number}  id id为云主机的ID
@apiParam {String}  name　云硬盘名称。（例如: i-testvolume）

@apiSuccess {Number} id     任务的ID
@apiSuccess {Number} name   任务的名称
@apiSuccess {Number} server     云主机的名称
@apiSuccess {Number} status     任务的状态: queue, running, success, fail
@apiSuccess {Number} finished   任务是否完成
@apiSuccess {Number} created_at     任务创建时间
@apiSuccess {Number} finished_at    任务完成时间
@apiSuccessExample {Array} 返回数据:
返回值类型: Hash
返回内容为任务的详细信息, Hash中Key的说明信息:
{
  "status": "queue",
  "name": "restoretemplate",
  "created_at": "2015-09-14 12:36:47",
  "server": "i-jzgoiesw",
  "finished": false,
  "id": 58
}
"""
