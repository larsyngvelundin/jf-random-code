<?php
$jotform_form_id = '';
$jotform_api_key = '';

// mockdata for testing:
$name_first = 'John';
$name_last = 'Smith';
$email = 'example@example.com';
$portfolio_instagram = 'profilehandle';
$exhib_title = 'Title';
$technology_needed = '';
$hashtags = array('#test', '#photo');

// Using Field IDs instead of Unique Names
$jotform_data = array(
    '3_first' => $name_first,
    '3_last' => $name_last,
    '4' => $email,
    '12' => $portfolio_instagram,
    '8' => $exhib_title,
    '9' => $technology_needed,
    '11' => implode(', ', $hashtags)
);
$url = "https://api.jotform.com/form/" . $jotform_form_id . "/submissions";
$ch = curl_init($url);
// Using header key for apiKey
curl_setopt($ch, CURLOPT_HTTPHEADER, array(
    'Content-Type: application/json',
    'apiKey:' . $jotform_api_key
));
curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($jotform_data));
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
$response = curl_exec($ch);
$http_status = curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);
?>