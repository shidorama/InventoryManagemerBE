# Endpoints

* `/boxes`
    * **GET**
        * Fields: None
        * Description: Get list of all boxes registered 
    * **POST**
        * Description: Create new box
        * Fields:
            * Name - box name
            * Picture - file, optional
            * Root box - box that this one is resides inside
        * Response
            * Status: OK|ERROR
            * Box ID: uuid
            
* `/boxes/{uuid}`
    * **GET**
        * Description: Get box image, description, contents and QR
    * **PATCH**
        * Description: Change box fields
        
* `/boxes/{uuid}/items`
    * **GET**
        * Description: get all items in a box
    * **POST**
        * Add new item
        * Fields: name, picture
    * **DELETE**
        * Empty the box
        
* `/boxes/{uuid}/items/{uuid}`
    * **GET**
        * Get item info 
    * **DELETE**
        * Remove item from a box
    * **PATCH**
        * change item info / move to another box