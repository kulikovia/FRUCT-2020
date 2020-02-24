PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX my: <http://127.0.0.1/bg/ont/test1#>
SELECT * 
WHERE
{
  ?Accounts my:includes_user ?User_account .
  ?Accounts my:has_tariff_plan "Promo" .
  ?User my:has_id ?User_account .
  ?Device my:is_connected_to_hub "H1" .
  ?Device my:has_the_device_model "Moto2k" .	
  ?Device my:has_id ?Device_id .
  ?User my:uses_device ?Device_id  .
  ?User my:requests ?Request_ID .
  ?Request_ID rdf:property ?Date
  FILTER contains(?Date, "2020-02-01") .
  ?Request_ID my:request_detailes ?Detailes_ID .
  ?Detailes_ID rdf:subject "WatchTV" .
  ?Detailes_ID rdf:object ?Asset_ID .
  ?Asset_ID my:has_id "Asset1"
}
