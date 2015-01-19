<?php

$MailChimp = new \Drewm\MailChimp('8011a2778610a68cbc6916579bb0a4a1-us10');
$result = $MailChimp->call('lists/subscribe', array(
                'id'                => '8842712456',
                'email'             => array('email'=>$_POST['email']),
//                'merge_vars'        => array('FNAME'=>'Davy', 'LNAME'=>'Jones'),
                'double_optin'      => false,
                'update_existing'   => true,
                'replace_interests' => false,
                'send_welcome'      => false,
            ));
print_r($result);

