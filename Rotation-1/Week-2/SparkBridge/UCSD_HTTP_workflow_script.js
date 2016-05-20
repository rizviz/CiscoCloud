// Note: this code is a slightly modified verison of Sabina Al Farah and Orf Gelbrich's UCSD HTTP Integration Package
// The only modifications was to examine the returned output for 'ok' or 'error'

importPackage(java.io);
importPackage(org.apache.http);
importPackage(org.apache.http.client);
importPackage(org.apache.http.client.methods);
importPackage(org.apache.http.impl.client);
importPackage(java.lang);
importPackage(java.util);
importPackage(com.cloupia.model.cIM);
importPackage(com.cloupia.service.cIM.inframgr);
importPackage(org.apache.http.entity);


function WebServiceAccess() {
  var httpClient = new DefaultHttpClient();
  var inputMethod = input.inputMethod;
  var getRequest;
  var postRequest;
  var response;
  var br;
  var buffer;
  var payloadData;
  var requestSuccess;
  var outLine;

  logger.addInfo("input URL : " + input.URL + " accept header : " + input.acceptHeader + "input payload : " + input.payload);
  try {
    if(inputMethod == "GET") {
      getRequest = new HttpGet(input.URL);
      getRequest.addHeader("accept", input.acceptHeader);
      response = httpClient.execute(getRequest);
    } else {
        postRequest = new HttpPost(input.URL);
        postRequest.addHeader("accept", input.acceptHeader);
        payloadData = new StringEntity(input.payload);
        postRequest.setEntity(payloadData); 
        response = httpClient.execute(postRequest); 
      }

    if (response.getStatusLine().getStatusCode() != 200) {
      logger.addError("Failed : HTTP error code : " + response.getStatusLine().getStatusCode());
    }
    br = new BufferedReader(new InputStreamReader((response.getEntity().getContent())));   
    buffer = new StringBuffer();
  	logger.addInfo("Output from Server .... \n");
  	while ((outLine = br.readLine()) != null) {
      buffer.append(outLine);
    }

    if (buffer.toString() == 'ok') {
        requestSuccess = true; }
    else {
        requestSuccess = false; }

    output.strResult =  buffer.toString();
    httpClient.getConnectionManager().shutdown();                                            
  } 
  catch (e) {
  	logger.addInfo(e)
  	ctxt.setFailed("web service request failed : " + e.message);
  } 
}

WebServiceAccess();

