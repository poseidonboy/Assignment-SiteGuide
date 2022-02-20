  var ws= new WebSocket('ws://127.0.0.1:8000/vehicle/')
  
  ws.onopen= function(){
      console.log("websocket Connected noow open")
     

  }
  ws.onmessage=function(event){     
      console.log("onmessage working")
      // const data=JSON.parse(event.data)
      console.log(event.data)
      newdata=data
      
    
  }

   
  document.getElementById('addbtnid').onclick= function(event){
    const nameInputDom=document.getElementById('nameid')
    const name=nameInputDom.value
    const vnoInputDom=document.getElementById('vnoid')
    const vno=vnoInputDom.value
    const speedInputDom=document.getElementById('speedid')
    const speed=speedInputDom.value
    const avgspeedInputDom=document.getElementById('avgspeedid')
    const avgspeed=avgspeedInputDom.value
    const tempInputDom=document.getElementById('tempid')
    const temp=tempInputDom.value
    const fuelInputDom=document.getElementById('fuelid')
    const fuel=fuelInputDom.value
    const engineInputDom=document.getElementById('engstatusid')
    const engine=engineInputDom.value
    ws.send(JSON.stringify({
        'name':name,
        'vno':vno,
        'speed':speed,
        'avgspeed':avgspeed,
        'temp':temp,
        'fuel':fuel,
        'engine':engine
    }))
    nameInputDom.value=''
    vnoInputDom.value=''
    speedInputDom.value=''
    avgspeedInputDom.value=''
    tempInputDom.value=''
    fuelInputDom.value=''
    engineInputDom.value=''
}