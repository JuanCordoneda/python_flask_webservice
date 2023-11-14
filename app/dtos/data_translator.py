#app/dtos/data_translator.py
# that file translate every request and response

# ESTO SE APLICA EN LA API PAGOS PYME
# ESTO TRADUCE LAS REQUEST Y RESPONSES CUANDO ES NECESARIO HACER SWITH ENTRE ESPAñOL E INGLES
# LAS REQUESTS SON ENVIADAS EN INGLES Y SE TRADUCEN A ESPAñOL
# LOS RESPONSES AL REVEZ, DE ESPAñOL A INGLES
# -----------------------------------------------------------------------
# ------------------------- PRODUCT TRANSLATIONS ------------------------
# -----------------------------------------------------------------------

# ACA SE MANDA LA RESPONSE EN ESPAñOL Y SE TRADUCE A INGLES
def translate_get_products_response(data):
    try:
        response = []
        for item in data:
            transformed_item = {
                "product_id": item["idProducto"],
                "external_id": item["externalId"],
                "description": item["descripcion"],
                "category": item["rubro"],
                "transaction_type": item["tipoTransaccion"],
                "fraud_check_required": item["fraudCheckRequired"],
                "enable_payment_button": item["habilitadoBotonDePago"],
                "enable_payment_link": item["habilitadoLinkDePago"],
                "enable_web_portal": item["habilitadoPortalWeb"],
                "vesta_score_limit": item["limiteScoreVesta"],
                "merchant_routing_id": item["merchantRoutingId"],
                "hide_debt_description": item["ocultarDescripcionDeuda"],
                "preferred_order": item["ordinalPreferido"],
                "parameters": [
                    {
                        "description": param["descripcion"],
                        "group": param["grupo"],
                        "length": param["largo"],
                        "optional": param["opcional"],
                        "order": param["ordinal"],
                        "help_text": param["textoAyuda"],
                        "data_type": param["tipoDato"]
                    }
                    for param in item["parametros"]
                ],
            }
            response.append(transformed_item)
        return response
    except Exception as e:
        return Exception(f"Error translating data: {str(e)}")

# ACA SE MANDA LA REQUEST EN INGLES Y SE TRADUCE A ESPAñOL
def translate_post_product_request(data):
    try:
        request = {'idProducto': data['product_id'], 'datosAdicionales': []}
        if data.get('extra_data'):
            for extra_item in data['extra_data']:
                request['datosAdicionales'].append({
                    'ordinal': extra_item['ordinal'],
                    'valor': extra_item['value']
                })
        return request
    except Exception as e:
        return Exception(f"Error translating data: {str(e)}")

def translate_post_product_response(data):
    try:
        response = []
        for item in data['transacciones']:
            transformed_item = {
                "product_id": item.get("idProducto", None),
                "transaction_id": item.get("idTransaccion", None),
                "requires_additional_data": item.get("requiereDatosAdicionales", None),
                "currency": item.get("moneda", None),
                "amount": item.get("importe", None),
                "minimum_amount": item.get("importeMinimo", None),
                "maximumAmount": item.get("importeMaximo", None),
                "description": item.get("descripcion", None),
                "variableAmount": item.get("importeVariable", None)
            }
            response.append(transformed_item)
        return response
    except Exception as e:
        return Exception(f"Error translating data: {str(e)}")

# -----------------------------------------------------------------------
# ------------------------- TRANSACTION TRANSLATIONS --------------------
# -----------------------------------------------------------------------

def translate_get_transaction_response(data):
    try:
        response = {
            "transaction_id": data["idTransaccion"],
            "barcode": data["codigoBarras"],
            "product": data["producto"],
            "amount": data["monto"],
            "currency": data["moneda"],
            "description": data["descripcion"],
            "status": data["estado"],
            "remarks": data["observaciones"],
            "receipt": data["comprobante"],
            "date": data["fecha"],
            "reconciled": data["conciliada"],
        }
        return response
    except Exception as e:
        return Exception(f"Error translating data: {str(e)}")

# -----------------------------------------------------------------------
# ------------------------- INVOICES TRANSLATIONS -----------------------
# -----------------------------------------------------------------------

def translate_post_invoice_request(data):
    try:
        request = {'codigoBarras': data['barcode'], 'datosAdicionales': []}
        for item in data['extra_data']:
            item = {'ordinal': item['ordinal'], 'valor': item['value']}
            request['datosAdicionales'].append(item)
        return request
    except Exception as e:
        return Exception(f"Error translating data: {str(e)}")

def translate_post_invoice_response(data):
    try:
        response = []
        transformed_item = {
            "transaction_id": data.get("idTransaccion", None),
            "requires_additional_data": data.get("requiereDatosAdicionales", None),
            "currency": data.get("moneda", None),
            "amount": data.get("importe", None),
            "minimum_amount": data.get("importeMinimo", None),
            "maximumAmount": data.get("importeMaximo", None),
            "description": data.get("descripcion", None),
            "variableAmount": data.get("importeVariable", None)
        }
        response.append(transformed_item)
        return response
    except Exception as e:
        return Exception(f"Error translating data: {str(e)}")

# -----------------------------------------------------------------------
# ------------------------- BATCHES TRANSLATIONS -------------------------
# -----------------------------------------------------------------------

def translate_post_batche_request(data):
    try:
        return {'idTransaccion': data['idTransaction']}
    except Exception as e:
        return Exception(f"Error translating data: {str(e)}")

def translate_post_batche_response(data):
    try:
        transaction_data = data["transaccion"]
        response = {
            "status": data["estado"],
            "lot_id": data["idLote"],
            "total": data["total"],
            "transaction": {
                "apiBillersBillerId": transaction_data["apiBillersBillerId"],
                "apiBillersDescription": transaction_data["apiBillersDescripcion"],
                "apiBillersKey": transaction_data["apiBillersKey"],
                "voucher": transaction_data["comprobante"],
                "description": transaction_data["descripcion"],
                "status": transaction_data["estado"],
                "transaction_id": transaction_data["idTransaccion"],
                "amount": transaction_data["importe"],
                "currency": transaction_data["moneda"],
                "account_number": transaction_data["numeroCuenta"],
                "remarks": transaction_data["observaciones"],
                "record": transaction_data["registro"],
                "lot_sequence": transaction_data["secuenciaLote"],
                "tracking_id": transaction_data["trackingId"]
            }
        }
        return response
    except Exception as e:
        return Exception(f"Error translating data: {str(e)}")
