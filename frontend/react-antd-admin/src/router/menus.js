/**
 * @ Author: Jone Chen
 * @ Create Time: 2019-06-19 16:58:23
 * @ Modified by: Jone Chen
 * @ Modified time: 2019-07-18 16:09:41
 * @ Description:权限控制，permission 1==超级管理员，其它为普通用户
 */

export const menus = [
	{
		path: '/dashboard',
		title: '首頁',
		icon: 'home'
	},
	{
		path: '/icon',
		title: '圖標',
		icon: 'file'
	},
	{
		path: '/form',
		title: '表單',
		icon: 'form',
		children: [
			{
				path: '/form/basic',
				title: '基本表單'
			},
			{
				path: '/form/editor',
				title: 'editor'
			},
			{
				path: '/form/markdown',
				title: 'MarkDown'
			}
		]
	},
	{
		path: '/menu',
		title: '多級菜單',
		icon: 'menu',
		children: [
			{
				path: '/menu/level',
				title: '二級菜單',
				children: [
					{
						path: '/menu/level/submenu-1',
						title: '三級菜單',
					},
					{
						path: '/menu/level/submenu-2',
						title: '三級菜單_2'
					}
				]
			}
		]
	},
	{
		path: '/table',
		title: '表格',
		icon: 'table',
		children: [
			{
				path: '/table/basic',
				title: 'basic表格'
			},
			{
				path: '/table/edit',
				title: '表格編輯'
			},
			{
				path: '/table/search',
				title: '表格搜索'
			}
		]
	},
	{
		path: '/chart',
		title: '圖表',
		icon: 'area-chart',
		children: [
			{
				path: '/chart/line',
				title: '折線圖'
			},
			{
				path: '/chart/keyboard',
				title: '鍵盤圖表'
			},
			{
				path: '/chart/bar',
				title: '柱狀圖'
			},
			{
				path: '/chart/pie',
				title: '餅圖'
			},
			{
				path: '/chart/mixin',
				title: '混合圖表'
			}
		]
	},
	{
		path: '/control',
		title: '控制區',
		icon: 'control',
		children: [
			{
				path: '/control/tree',
				title: '樹狀控制區'
			},
			{
				path: '/control/select',
				title: '選擇器'
			},
			{
				path: '/control/other',
				title: '其它'
			}
		]
	},
	{
		path: '/permission',
		title: '權限測試',
		icon: 'safety-certificate',
		children: [
			{
				path: '/permission/toggle',
				title: '權限切換',
				permission: 1
			},
			{
				path: '/permission/intercept',
				title: '路由攔截'
			}
		]
	},
	{
		path: '/news',
		title: '消息',
		icon: 'bell'
	},
	{
		path: '/error',
		title: '錯誤訊息',
		icon: 'switcher',
		children: [
			{
				path: '/error/404',
				title: '404'
			},
			{
				path: '/error/500',
				title: '500'
			}
		]
	},
	{
		path: '/about',
		title: '關於',
		icon: 'copyright'
	},
	{
		path: '/personInfo',
		title: '處方系統',
		icon: 'copyright'
	},
	{
		path: '/VideoRecorder',
		title: '個人信息',
		icon: 'copyright'
	},
	{
		path: '/connectBackend',
		title: '後端接口',
		icon: 'copyright'
	}

];
