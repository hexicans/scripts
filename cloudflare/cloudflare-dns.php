#!/usr/bin/php
<?php
/**
 * Script by Phantium
 */

class CloudFlareDNS {
        private $api_url, $api_params, $request_url;

        private $username = "cloudflare_username";
        private $apikey = "cloudflare_apikey";

        function getIP() {
                $ip_url = file_get_contents('http://ip.raw.re');
                $this->ip = $ip_url;
                if (strlen($this->ip) < 10) {
                        return false;
                } else {
                        return $this->ip;
                }
        }

        function setIP($hostname) {
                if ($this->getIP() === false) {
                        echo "Error: IP was not succesfully retrieved.";
                        return;
                }
                $this->api_url = "https://www.cloudflare.com/api_json.html";
                $this->api_params = "?a=DIUP&hosts=". $hostname ."&u=". $this->username .
                                    "&tkn=". $this->apikey ."&ip=". $this->getIP();
                $this->request_url = $this->api_url . $this->api_params;
                try {
                        $this->result = file_get_contents($this->request_url);
                }
                catch (Exception $e) {
                        echo "ERROR, Caught exception:", $e->getMessage(), "\n";
                        return;
                }
                return $this->result."\n";
        }
}

$cf = new CloudFlareDNS;
echo $cf->setIP('dns.yourdomain.com');

