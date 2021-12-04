let currentTab = null;

browser.tabs.onActivated.addListener((event) => currentTab = event.tabId);
setInterval(updateBrowserTime,1000);
async function updateBrowserTime() {
  if(!currentTab)
    return;
  let frames = null;
  try {
    frames = await browser.webNavigation.getAllFrames({'tabId':currentTab});
  } catch(error){
    console.log(error);
  }
  let frame = frames.filter((frame) => frame.parentFrameId == -1)[0];
  if(!frame.url.startsWith('http'))
    return;
  let hostname = new URL(frame.url).hostname;
  try {
    let seconds = await browser.storage.local.get({[hostname]:0});
    browser.storage.local.set({[hostname]:seconds[hostname] + 1});
  } catch(error){
    console.log(error)
  }
}
setInterval(sendTabToPython,3000);
async function sendTabToPython()
{
  let tab = await browser.storage.local.get(null);
  console.log(tab)
  await fetch('http://127.0.0.1:5000/akjksHBJJ56qsS:$skjs61SS2xcxcdf46SD$.',{
    //declare what type of data we are sending
    headers : {'Content-Type': 'application/json'},
    //Specify the method
    method:'POST',
    // A JSON payload
    body:JSON.stringify(tab)

  }).then(function (response){ // At this point, Flask has printed our JSON
    return response.text();
  }).then(function (tab) {
    console.log('POST response: ');
    console.log(tab);
  })
}
