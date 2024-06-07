                                                          
        
String[] keyValue = healthHistoryQuestion.split(":");
                        if (keyValue.length >= 2) {
                            healthHistoryMap.put(keyValue[0], keyValue[1]);
------------------------------------ 
if(expDateOpt.isPresent()){ 
                String expString = expDateOpt.get().split(":")[userProfileIdKeyValueOpt.get().split(":").length-1];
                long longDate = Long.parseLong(expString + "000");

------------------------------------  


------------------------------------


------------------------------------       


------------------------------------



eyJhbGciOiJSUzI1NiIsImtpZCI6IjMyQUM0OUFFNTU3RTk0MzlEQkNCRkZDNDJCMkIxMjMzMUIzMzlBQkUiLCJ0eXAiOiJhdCtqd3QiLCJ4NXQiOiJNcXhKcmxWLWxEbmJ5X19FS3lzU014c3ptcjQifQ.eyJuYmYiOjE1OTMwNjIzMDksImV4cCI6MTc1MDg0NzA2OSwiaXNzIjoiaHR0cDovL2tvbmEtZGV2LWFwaS5icmllcmxleWNsb3VkLm5ldC9pZGVudGl0eSIsImF1ZCI6WyJrb25hLWNvcmUtYXBpcyIsIklkZW50aXR5U2VydmVyQXBpIl0sImNsaWVudF9pZCI6ImtvbmFfdnVlX2FwcCIsInN1YiI6ImEzNmZkZTM2LWY0YmYtNDI4Mi05OTZhLWEwZDE1OTRlZTAyMSIsImF1dGhfdGltZSI6MTU5MzA2MjMwNCwiaWRwIjoibG9jYWwiLCJlbWFpbCI6ImxveWFsdHlBZG1pbkBrb25hLmNvbSIsInJvbGUiOiJhZG1pbiIsInRlbmFudCI6IkJSSUVSTEVZIiwiZGVmYXVsdEFwcCI6Im15RGVmYXVsdEFwcCIsIm5hbWUiOiJsb3lhbHR5QWRtaW5Aa29uYS5jb20iLCJzY29wZSI6WyJ1c2VyLWluZm8iLCJlbWFpbCIsInByb2ZpbGUiLCJvcGVuaWQiLCJrb25hLWNvcmUtYXBpcyIsIklkZW50aXR5U2VydmVyQXBpIl0sImFtciI6WyJwd2QiXX0.pZD5TYCs6VY-5yIy8uEcTV8RabIXxY-HzN-ElK9P9Yc513XQ2A-GWxxQ4gyM_D4U4HklO1PK2JSb3SLxbsEpvVY15qXNyeKa4TUQknSuSalZa7XT1OWS9QwgVnQAbmVjDuyzuRBqxMupD096otiymGe9k_bTrxHA2lOUt26WeXgS-rrHtuypLgoSnrI9oABFOHfxffXc4zoshp3plb5nZmm0EgxXGhY3f_HQDjf5U6merTDMn5ua5ccZmcLsn6AwX1pS6EHmHcZ310oLPa5rhypzSOWrszCBxaOlysWKIRUGbfgN8hCO-id3LrPukoICPGtQIgMMhtI2NqI_RPXLvA
 eyJhbGciOiJSUzI1NiIsImtpZCI6IjMyQUM0OUFFNTU3RTk0MzlEQkNCRkZDNDJCMkIxMjMzMUIzMzlBQkUiLCJ0eXAiOiJhdCtqd3QiLCJ4NXQiOiJNcXhKcmxWLWxEbmJ5X19FS3lzU014c3ptcjQifQ.eyJuYmYiOjE1OTMwNjIzMDksImV4cCI6MTc1MDg0NzA2OSwiaXNzIjoiaHR0cDovL2tvbmEtZGV2LWFwaS5icmllcmxleWNsb3VkLm5ldC9pZGVudGl0eSIsImF1ZCI6WyJrb25hLWNvcmUtYXBpcyIsIklkZW50aXR5U2VydmVyQXBpIl0sImNsaWVudF9pZCI6ImtvbmFfdnVlX2FwcCIsInN1YiI6ImEzNmZkZTM2LWY0YmYtNDI4Mi05OTZhLWEwZDE1OTRlZTAyMSIsImF1dGhfdGltZSI6MTU5MzA2MjMwNCwiaWRwIjoibG9jYWwiLCJlbWFpbCI6ImxveWFsdHlBZG1pbkBrb25hLmNvbSIsInJvbGUiOiJhZG1pbiIsInRlbmFudCI6IkJSSUVSTEVZIiwiZGVmYXVsdEFwcCI6Im15RGVmYXVsdEFwcCIsIm5hbWUiOiJsb3lhbHR5QWRtaW5Aa29uYS5jb20iLCJzY29wZSI6WyJ1c2VyLWluZm8iLCJlbWFpbCIsInByb2ZpbGUiLCJvcGVuaWQiLCJrb25hLWNvcmUtYXBpcyIsIklkZW50aXR5U2VydmVyQXBpIl0sImFtciI6WyJwd2QiXX0.pZD5TYCs6VY-5yIy8uEcTV8RabIXxY-HzN-ElK9P9Yc513XQ2A-GWxxQ4gyM_D4U4HklO1PK2JSb3SLxbsEpvVY15qXNyeKa4TUQknSuSalZa7XT1OWS9QwgVnQAbmVjDuyzuRBqxMupD096otiymGe9k_bTrxHA2lOUt26WeXgS-rrHtuypLgoSnrI9oABFOHfxffXc4zoshp3plb5nZmm0EgxXGhY3f_HQDjf5U6merTDMn5ua5ccZmcLsn6AwX1pS6EHmHcZ310oLPa5rhypzSOWrszCBxaOlysWKIRUGbfgN8hCO-id3LrPukoICPGtQIgMMhtI2NqI_RPXLvA 

      