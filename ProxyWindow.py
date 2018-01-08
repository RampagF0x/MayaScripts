# coding=utf-8
import maya.cmds as cmds
def ProxyWindow(any):
    if cmds.window('Proxy_optionsWindow', ex=True):
        cmds.deleteUI('Proxy_optionsWindow', wnd=True)
    win2 = cmds.window('Proxy_optionsWindow', title='Proxy_Window', widthHeight=(300, 200))
    cmds.columnLayout(adj=True)
    cmds.button(en=False, l='')
    cmds.button(l=u'Arnold代理')
    cmds.columnLayout(adj=True)
    cmds.button(l=u'Redshift代理')
    cmds.showWindow(win2)