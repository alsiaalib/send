
# Discord 消息发送指南

本指南将介绍如何使用GitHub Action和Discord API发送消息。

## 1. 原理

以下是一个使用`curl`命令发送POST请求到Discord API的示例。该命令包括必要的头部信息和请求数据。

```bash
curl -X POST \
-H "Content-Type: application/json" \
-H "Authorization: ODU2NXYvtjb7g " \
-d "{\"mobile_network_type\":\"wifi\",\"content\":\"l681w\",\"nonce\":\"1289965167660390794\",\"tts\":false,\"flags\":0}" \
https://discord.com/api/v9/channels/1279755843830677518/messages
```
该api通过浏览器f12获取
 

## 2. 步骤

### 获取Authorization Token

要获取Discord的Authorization Token，请按照以下步骤操作：

1. 访问 [DiscordChatExporter文档](https://github.com/Tyrrrz/DiscordChatExporter/tree/master/.docs)。
2. 在Chrome浏览器中打开Discord，然后按`F12`打开开发者工具。
3. 转到`Console`标签页，并粘贴以下代码片段到控制台中执行：

`(webpackChunkdiscord_app.push([[''],{},e=>{m=[];for(let c in e.c)m.push(e.c[c])}]),m).find(m=>m?.exports?.default?.getToken!==void 0).exports.default.getToken()`
 

执行上述代码后，将看到Authorization Token。
#### 3.1 注意，f12中network，以curl复制底下的链接，也有token，相当于复制了所有token

### 创建GitHub Action
#### 首先fork此仓库
接下来，需要开启一个GitHub Action来发送消息：

1. 在您的GitHub仓库顶部，创建一个新的 Actions，选择顶部Code、 Issue 右侧的Action 确定开启

```
2. 如果是自己创建仓库，则开启后需要编写yml代码，详见下步骤3
3. 创建action后 选择 set up a workflow yourself自己填写，如下所示：
这其实就是相当于创建了一个 `.github/workflows` 文件夹下的yml后缀的txt文件
```


4. 在GitHub仓库的设置（Settings）中，转到`Secrets`部分。
5. 点击`New secret`按钮，设置名称为`TOKEN`，并将之前获取的Token作为秘密值。

现在，每次编辑代码时，GitHub Action都会运行，并使用您的Token发送消息到指定的Discord频道。
注意需要自己在代码中加个空格，更新一次代码，才会运作，之后就是每天运行5.5小时，每1分钟发送一次
 

请确保在实际使用中替换示例中的Token和其他敏感信息，并且遵循GitHub和Discord的使用条款和隐私政策。
