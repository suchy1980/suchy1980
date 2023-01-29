*** Settings ***
Library               RequestsLibrary
*** Variables ***
${client}   Lukasz
${mail}     lukasz@example.com
${http}     https://simple-books-api.glitch.me
${token}
*** Test Cases ***
GET_STATUS
    ${get_response}    GET    ${http}/status
    Log to console    status ${get_response}
GET_BOOKS
    ${get_response}    GET    ${http}/books
    Log to console    status ${get_response}
POST_REGISTRATION
    ${register_json}    create dictionary    clientName=${client}    clientEmail=${mail}
    ${post_register_response}    POST    ${http}/api-clients/
    ...                                                            json=${register_json}
#ORDER
#    ${headers}    create dictionary    Content-Type=application/json    Authorization=Bearer ${token}
#    ${order_body}    create dictionary   bookId=4    customerName=${client}
#    ${post_order_response}    POST    ${http}/orders
#        ...                                           headers=${headers}    json=${order_body}
