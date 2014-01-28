<?php
define('WS_COMERCIO', '55');
define('LEERE_URI', 'http://ws.leer-e.es/wsdl/');

/**
 * Clase para interactuar con los WebServices de Leer-e
 *
 * @author Jon Husillos (Biko)
 * @date 2009-11
 */
class wsLeere {
	/**
	 * Constructor
	 *
	 * @public
	 */
	private $token;
	public $client;
	public $msg;
	private $response;
	
	public function __construct($idClienteComercio=0, $debug=0){
		if ((int)$idClienteComercio!=0){
			$this->login($idClienteComercio);
		}else{
			$this->token=null;
		}
	}
	
	public function __destruct(){
	}
	
	private function do_call($wsdl, $method, $params){
		$uriWS= LEERE_URI . $wsdl.'.wsdl';
		$this->client = new SoapClient($uriWS, array(
			"actor" => "urn:BasicAPI",
			"soap_version" => SOAP_1_2
		));	
		$this->msg = new SoapVar($params, SOAP_ENC_OBJECT);

		$this->response = $this->client->$method($this->msg);
        var_dump($this->response);
		return(json_encode($this->response));
	}
	

	public function login($idClienteComercio){
		$params=array(
			"IdComercio" => WS_COMERCIO,
			"IdClienteComercio" => $idClienteComercio
		);
		$this->token=$this->do_call('usuarios','login', $params);
		return ($this->token);
	}
	
	public function addAparato($nombreAparato,$PIDAparato,$tipoAparato=2135){
		if ($this->token){
			$params=array(
				"token" => $this->token,
				"nombreAparato" => $nombreAparato,
				"PIDAparato" => $PIDAparato,
				"tipoAparato" => $tipoAparato
			);
			return ($this->do_call('usuarios','addAparato', $params));
		}else{
			return (0);
		}
	}

	public function delAparato($PIDAparato){
		if ($this->token){
			$params=array(
				"token" => $this->token,
				"PIDAparato" => $PIDAparato
			);
			return ($this->do_call('usuarios','delAparato', $params));
		}else{
			return (0);	
		}
	}

	public function getAparatos(){
		if ($this->token){
			$params=array(
				"token" => $this->token
			);
			return ($this->do_call('usuarios','getAparatos', $params));
		}else{
			return (0);	
		}
	}
	
	public function getDatosCliente(){
		if ($this->token){
			$params=array(
				"token" => $this->token
			);
			return ($this->do_call('usuarios','getDatosCliente', $params));
		}else{
			return (0);	
		}
	}	

	public function getLibrosCliente($idLibro=0,$idModelo=0){
		if ($this->token){
			$params=array(
				"token" => $this->token,
				"idLibro" => intval ($idLibro),
				"idModelo" => intval ($idModelo)
			);
			return ($this->do_call('usuarios','getLibrosCliente', $params));
		}else{
			return (0);	
		}
	}

	public function validarCupon($IdCupon,$IdPedido){
		if ($this->token){
			$params=array(
				"token" => $this->token,
				"IdCupon" => $IdCupon,
				"IdPedido" => $IdPedido
			);
			return ($this->do_call('cupones','validarCupon', $params));
		}else{
			return (0);
		}
	}

	public function getDetalleLibro($idLibro=0,$idModelo=0){
		if ($idLibro){
			$params=array(
				"IdComercio" => (int)WS_COMERCIO,
				"IdLibro" => $idLibro,
				"IdModelo" => $idModelo
			);
			return ($this->do_call('libros','getDetalleLibro', $params));
		}else{
			return (0);	
		}
	}

	public function addLibroCliente($idLibro=0,$idModelo=0,$idPedido=0,$test=0){
		if ($idLibro && $idModelo && $idPedido){
			$params=array(
				"token" => $this->token,
				"IdLibro" => $idLibro,
				"IdModelo" => $idModelo,
				"IdPedido" => $idPedido,
				"test" => $test
			);
			return ($this->do_call('libros','addLibroCliente', $params));
		}else{
			return (0);	
		}
	}
	
	public function getGeneros($IdGenero=0){
		$params=array(
			"IdComercio" => WS_COMERCIO,
			"IdGenero" => intval($IdGenero)
		);	
		return ($this->do_call('genero','getGeneros', $params));
	}
	
	public function getEditoriales($IdEditorial=0){
		$params=array(
			"IdComercio" => WS_COMERCIO,
			"IdEditorial" => intval($IdEditorial)
		);	
		return ($this->do_call('editorial','getEditoriales', $params));
	}	
	
	public function getAutores($IdAutor=0){
		$params=array(
			"IdComercio" => WS_COMERCIO,
			"IdAutor" => intval($IdAutor)
		);	
		return ($this->do_call('autor','getAutores', $params));
	}
	public function getModelos($IdModelo=0){
		$params=array(
			"IdComercio" => WS_COMERCIO,
			"IdModelo" => intval($IdModelo)
		);	
		return ($this->do_call('modelo','getModelos', $params));
	}
	
	public function getCatalogo($IdAutor=0,$IdGenero=0,$IdEditorial=0){
		$params=array(
			"IdComercio" => WS_COMERCIO,
			"IdAutor" => intval($IdAutor),
			"IdGenero" => intval($IdGenero),
			"IdEditorial" => intval($IdEditorial)
		);	
		return ($this->do_call('catalogo','getCatalogo', $params));
	}	
	
}
?>
