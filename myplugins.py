# coding=utf-8
import maya.cmds as cmds
import maya.mel as mel
import sys
import subprocess

print sys.version
version = sys.version
plugins = cmds.pluginInfo(query=True, pluginsInUse=True)

'''显示项目路劲'''
def showworkspace(scene):
    curlworkspace = cmds.workspace(q=True, directory=True)
    cmds.confirmDialog(t='项目路径',m=curlworkspace,b='OK')
'''显示场景插件信息'''


def showPlugins(sence):
    if plugins == None:
        cmds.confirmDialog(t='提示', m='场景未使用插件', b='OK')
    else:
        cmds.confirmDialog(t='提示', m=",".join(plugins), b='OK')


'''显示FumeFX缓存'''


def showFumeFX(fumeNodes):
    fumeNodes = cmds.ls(type='ffxDyna')
    if 'ffxDyna' in cmds.ls(showType=True):
        AllPath = []
        for i in fumeNodes:
            fumeNode = i
            # print fumeNode
            defaultPath = cmds.fumeFXcmd(fumeNode, getPath='default')
            waveletPath = cmds.fumeFXcmd(fumeNode, getPath='wavelet')
            retimerPath = cmds.fumeFXcmd(fumeNode, getPath='retimer')
            illummapPath = cmds.fumeFXcmd(fumeNode, getPath='illummap')
            start_frames = cmds.getAttr(fumeNode + '.playback_start_frame')
            end_frames = cmds.getAttr(fumeNode + '.playback_end_frame')
            AllPath.append(fumeNode)

            # print start_frames
            fumeLists = [defaultPath, waveletPath, retimerPath]

            for l in fumeLists:
                start = l[:-4] + str("%04d" % start_frames) + '.fxd'
                AllPath.append(start)
            for l in fumeLists:
                end = l[:-4] + str("%04d" % end_frames) + '.fxd'
                # print l[:-4]+str("%04d" % start_frames)+'.fxd'
                # print l[:-4]+str("%04d" % end_frames)+'.fxd'
                # print start
                # print end
                AllPath.append(end)

                # print ",\r".join(AllPath)
        cmds.confirmDialog(t='提示', m=",\r".join(AllPath), b='OK')
    else:
        cmds.confirmDialog(t='提示', m='未使用FumeFX插件', b='OK')


'''show realflow cache'''
'''def showrfcache(sence):'''
'''defined realflow Mesh Nodes'''
rfmeshnodes = cmds.ls(type='RealflowMesh')
# print rfmeshnodes
'''defined realfow Particle Nodes'''
rfemitternodes = cmds.ls(type='RealflowEmitter')


def getrfmesh(rfmeshnodes):
    meshlist = []
    for i in rfmeshnodes:
        # print i
        '''show realflowMeshNodes'''
        meshpath = cmds.getAttr(i + '.Path')
        # print meshpath
        meshlist.append(meshpath)
    # print meshlist
    return meshlist


def Seqformat(type):
    if type == 0:
        return 'bin'
    elif type == 1:
        return 'pxy'
    elif type == 2:
        return 'rpc'


def nameformat(format, path, filename, padding, type):
    '''name.#.ext'''
    if format == 0:
        NameFormat = path + '/' + filename + '.0' + str(padding) + '%d' + '.' + Seqformat(type)
        '''name#.ext'''
    elif format == 1:
        NameFormat = path + '/' + filename + '0' + str(padding) + '%d' + '.' + Seqformat(type)
        '''name.ext.#'''
    elif format == 2:
        NameFormat = path + '/' + filename + '.' + Seqformat(type) + '0' + str(padding) + '%d'
        '''name_#.ext'''
    elif format == 3:
        NameFormat = path + '/' + filename + '_0' + str(padding) + '%d' + '.' + Seqformat(type)
    return NameFormat


def getrfparticle(rfemitternodes):
    particleSeqs = []
    for i in rfemitternodes:
        particleSeqs.append(i)
        list = cmds.getAttr(i + '.LoadSeqs')

        for a in range(len(list[0])):
            emitterpath = cmds.getAttr(i + '.Paths' + '[' + str(a) + ']')
            padding = cmds.getAttr(i + '.Paddings' + '[' + str(a) + ']')
            filename = cmds.getAttr(i + '.Prefixes' + '[' + str(a) + ']')
            type = cmds.getAttr(i + '.types' + '[' + str(a) + ']')
            format = cmds.getAttr(i + '.NameFormats' + '[' + str(a) + ']')
            partileseq = emitterpath + '/' + filename + '0' + str(padding) + '%d' + '.' + str(Seqformat(type))
            particleSeq = nameformat(format, emitterpath, filename, padding, type)
            particleSeqs.append(particleSeq)
    return particleSeqs
    print particleSeqs


def showRealfowcache(scene):
    if plugins == None:
        cmds.confirmDialog(t='提示', m='未使用Realflow插件', b='OK')
    else:
        if 'realflow' in plugins:
            # print 'yes'
            cmds.confirmDialog(t='realflowmesh', m=",\r".join(getrfmesh(rfmeshnodes)), b='OK')
            cmds.confirmDialog(t='realflowparticle', m=",\r".join(getrfparticle(rfemitternodes)), b='OK')
        else:
            cmds.confirmDialog(t='提示', m='未使用Realflow插件', b='OK')


def setViewport(arry):
    if cmds.window('vp_optionsWindow', ex=True):
        cmds.deleteUI('vp_optionsWindow', wnd=True)
    vp = cmds.window('vp_optionsWindow', title='ViewPort2.0', widthHeight=(500, 200))
    cmds.columnLayout(adj=True)
    cmds.showWindow(vp)
    # setVP2mode=mel.eval('optionVar -iv "viewportRenderer" 1')
    cmds.button(l='修改viewport2.0模式', c=setVP2mode)
    cmds.button(l='关闭maya', c=closeMaya)


def setVP2mode(give):
    mel.eval('optionVar -iv "viewportRenderer" 1')
    mel.eval('optionVar -sv "vp2RenderingEngine" "DirectX11"')
    cmds.confirmDialog(t='提示', m='需重启maya生效', b='OK')


def closeMaya(give):
    mel.eval('evalDeferred("quit")')
    # evn=mel.eval('$s=`getenv "PATH"`;')
    # subprocess.call('\"'+ sys.argv[0]+'\"', shell=True)

def cleanmysence(arry):
    mel.eval(('cleanUpScene 1'))

'''show window'''
if cmds.window('AR_optionsWindow', ex=True):
    cmds.deleteUI('AR_optionsWindow', wnd=True)
win = cmds.window('AR_optionsWindow', title='MyPlugins', widthHeight=(500, 200))
cmds.columnLayout(adj=True)
cmds.button(en=False, l='python ' + version)
cmds.button(l='显示场景插件', c=showPlugins)
cmds.button(l='查看项目路径',c=showworkspace)
cmds.button(l='显示FumeFX缓存文件', c=showFumeFX)
cmds.button(l='显示Realflow缓存文件', c=showRealfowcache)
cmds.button(l='设置maya2016视口模式', c=setViewport)
cmds.button(l='清理场景',c=cleanmysence)


cmds.showWindow(win)
