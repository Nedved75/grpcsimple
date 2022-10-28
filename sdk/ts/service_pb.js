/* eslint-disable */
/*Generated by GenDocu.com*/
// source: service.proto
/**
 * @fileoverview
 * @enhanceable
 * @suppress {missingRequire} reports error on implicit type usages.
 * @suppress {messageConventions} JS Compiler reports an error if a variable or
 *     field starts with 'MSG_' and isn't a translatable message.
 * @public
 */
// GENERATED CODE -- DO NOT EDIT!
/* eslint-disable */
// @ts-nocheck

var jspb = require('google-protobuf');
var goog = jspb;
var global = Function('return this')();

var google_protobuf_empty_pb = require('google-protobuf/google/protobuf/empty_pb.js');
goog.object.extend(proto, google_protobuf_empty_pb);
var google_api_annotations_pb = require('./google/api/annotations_pb.js');
goog.object.extend(proto, google_api_annotations_pb);
goog.exportSymbol('proto.gendocu.example.library_app.Author', null, global);
goog.exportSymbol('proto.gendocu.example.library_app.Book', null, global);
goog.exportSymbol('proto.gendocu.example.library_app.DeleteBookRequest', null, global);
goog.exportSymbol('proto.gendocu.example.library_app.DeleteBookRequest.SelectorCase', null, global);
goog.exportSymbol('proto.gendocu.example.library_app.ListBookResponse', null, global);
/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.gendocu.example.library_app.DeleteBookRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, proto.gendocu.example.library_app.DeleteBookRequest.oneofGroups_);
};
goog.inherits(proto.gendocu.example.library_app.DeleteBookRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  /**
   * @public
   * @override
   */
  proto.gendocu.example.library_app.DeleteBookRequest.displayName = 'proto.gendocu.example.library_app.DeleteBookRequest';
}
/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.gendocu.example.library_app.ListBookResponse = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.gendocu.example.library_app.ListBookResponse.repeatedFields_, null);
};
goog.inherits(proto.gendocu.example.library_app.ListBookResponse, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  /**
   * @public
   * @override
   */
  proto.gendocu.example.library_app.ListBookResponse.displayName = 'proto.gendocu.example.library_app.ListBookResponse';
}
/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.gendocu.example.library_app.Book = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.gendocu.example.library_app.Book, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  /**
   * @public
   * @override
   */
  proto.gendocu.example.library_app.Book.displayName = 'proto.gendocu.example.library_app.Book';
}
/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.gendocu.example.library_app.Author = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.gendocu.example.library_app.Author, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  /**
   * @public
   * @override
   */
  proto.gendocu.example.library_app.Author.displayName = 'proto.gendocu.example.library_app.Author';
}

/**
 * Oneof group definitions for this message. Each group defines the field
 * numbers belonging to that group. When of these fields' value is set, all
 * other fields in the group are cleared. During deserialization, if multiple
 * fields are encountered for a group, only the last value seen will be kept.
 * @private {!Array<!Array<number>>}
 * @const
 */
proto.gendocu.example.library_app.DeleteBookRequest.oneofGroups_ = [[1,2]];

/**
 * @enum {number}
 */
proto.gendocu.example.library_app.DeleteBookRequest.SelectorCase = {
  SELECTOR_NOT_SET: 0,
  ISBN: 1,
  TITLE: 2
};

/**
 * @return {proto.gendocu.example.library_app.DeleteBookRequest.SelectorCase}
 */
proto.gendocu.example.library_app.DeleteBookRequest.prototype.getSelectorCase = function() {
  return /** @type {proto.gendocu.example.library_app.DeleteBookRequest.SelectorCase} */(jspb.Message.computeOneofCase(this, proto.gendocu.example.library_app.DeleteBookRequest.oneofGroups_[0]));
};



if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * Optional fields that are not set will be set to undefined.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     net/proto2/compiler/js/internal/generator.cc#kKeyword.
 * @param {boolean=} opt_includeInstance Deprecated. whether to include the
 *     JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @return {!Object}
 */
proto.gendocu.example.library_app.DeleteBookRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.gendocu.example.library_app.DeleteBookRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Deprecated. Whether to include
 *     the JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.gendocu.example.library_app.DeleteBookRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.gendocu.example.library_app.DeleteBookRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    isbn: jspb.Message.getFieldWithDefault(msg, 1, ""),
    title: jspb.Message.getFieldWithDefault(msg, 2, "")
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.gendocu.example.library_app.DeleteBookRequest}
 */
proto.gendocu.example.library_app.DeleteBookRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.gendocu.example.library_app.DeleteBookRequest;
  return proto.gendocu.example.library_app.DeleteBookRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.gendocu.example.library_app.DeleteBookRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.gendocu.example.library_app.DeleteBookRequest}
 */
proto.gendocu.example.library_app.DeleteBookRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {string} */ (reader.readString());
      msg.setIsbn(value);
      break;
    case 2:
      var value = /** @type {string} */ (reader.readString());
      msg.setTitle(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.gendocu.example.library_app.DeleteBookRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.gendocu.example.library_app.DeleteBookRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.gendocu.example.library_app.DeleteBookRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.gendocu.example.library_app.DeleteBookRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = /** @type {string} */ (jspb.Message.getField(message, 1));
  if (f != null) {
    writer.writeString(
      1,
      f
    );
  }
  f = /** @type {string} */ (jspb.Message.getField(message, 2));
  if (f != null) {
    writer.writeString(
      2,
      f
    );
  }
};


/**
 * optional string isbn = 1;
 * @return {string}
 */
proto.gendocu.example.library_app.DeleteBookRequest.prototype.getIsbn = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 1, ""));
};


/**
 * @param {string} value
 * @return {!proto.gendocu.example.library_app.DeleteBookRequest} returns this
 */
proto.gendocu.example.library_app.DeleteBookRequest.prototype.setIsbn = function(value) {
  return jspb.Message.setOneofField(this, 1, proto.gendocu.example.library_app.DeleteBookRequest.oneofGroups_[0], value);
};


/**
 * Clears the field making it undefined.
 * @return {!proto.gendocu.example.library_app.DeleteBookRequest} returns this
 */
proto.gendocu.example.library_app.DeleteBookRequest.prototype.clearIsbn = function() {
  return jspb.Message.setOneofField(this, 1, proto.gendocu.example.library_app.DeleteBookRequest.oneofGroups_[0], undefined);
};


/**
 * Returns whether this field is set.
 * @return {boolean}
 */
proto.gendocu.example.library_app.DeleteBookRequest.prototype.hasIsbn = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional string title = 2;
 * @return {string}
 */
proto.gendocu.example.library_app.DeleteBookRequest.prototype.getTitle = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 2, ""));
};


/**
 * @param {string} value
 * @return {!proto.gendocu.example.library_app.DeleteBookRequest} returns this
 */
proto.gendocu.example.library_app.DeleteBookRequest.prototype.setTitle = function(value) {
  return jspb.Message.setOneofField(this, 2, proto.gendocu.example.library_app.DeleteBookRequest.oneofGroups_[0], value);
};


/**
 * Clears the field making it undefined.
 * @return {!proto.gendocu.example.library_app.DeleteBookRequest} returns this
 */
proto.gendocu.example.library_app.DeleteBookRequest.prototype.clearTitle = function() {
  return jspb.Message.setOneofField(this, 2, proto.gendocu.example.library_app.DeleteBookRequest.oneofGroups_[0], undefined);
};


/**
 * Returns whether this field is set.
 * @return {boolean}
 */
proto.gendocu.example.library_app.DeleteBookRequest.prototype.hasTitle = function() {
  return jspb.Message.getField(this, 2) != null;
};



/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.gendocu.example.library_app.ListBookResponse.repeatedFields_ = [1];



if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * Optional fields that are not set will be set to undefined.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     net/proto2/compiler/js/internal/generator.cc#kKeyword.
 * @param {boolean=} opt_includeInstance Deprecated. whether to include the
 *     JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @return {!Object}
 */
proto.gendocu.example.library_app.ListBookResponse.prototype.toObject = function(opt_includeInstance) {
  return proto.gendocu.example.library_app.ListBookResponse.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Deprecated. Whether to include
 *     the JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.gendocu.example.library_app.ListBookResponse} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.gendocu.example.library_app.ListBookResponse.toObject = function(includeInstance, msg) {
  var f, obj = {
    booksList: jspb.Message.toObjectList(msg.getBooksList(),
    proto.gendocu.example.library_app.Book.toObject, includeInstance)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.gendocu.example.library_app.ListBookResponse}
 */
proto.gendocu.example.library_app.ListBookResponse.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.gendocu.example.library_app.ListBookResponse;
  return proto.gendocu.example.library_app.ListBookResponse.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.gendocu.example.library_app.ListBookResponse} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.gendocu.example.library_app.ListBookResponse}
 */
proto.gendocu.example.library_app.ListBookResponse.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.gendocu.example.library_app.Book;
      reader.readMessage(value,proto.gendocu.example.library_app.Book.deserializeBinaryFromReader);
      msg.addBooks(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.gendocu.example.library_app.ListBookResponse.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.gendocu.example.library_app.ListBookResponse.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.gendocu.example.library_app.ListBookResponse} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.gendocu.example.library_app.ListBookResponse.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getBooksList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      1,
      f,
      proto.gendocu.example.library_app.Book.serializeBinaryToWriter
    );
  }
};


/**
 * repeated Book books = 1;
 * @return {!Array<!proto.gendocu.example.library_app.Book>}
 */
proto.gendocu.example.library_app.ListBookResponse.prototype.getBooksList = function() {
  return /** @type{!Array<!proto.gendocu.example.library_app.Book>} */ (
    jspb.Message.getRepeatedWrapperField(this, proto.gendocu.example.library_app.Book, 1));
};


/**
 * @param {!Array<!proto.gendocu.example.library_app.Book>} value
 * @return {!proto.gendocu.example.library_app.ListBookResponse} returns this
*/
proto.gendocu.example.library_app.ListBookResponse.prototype.setBooksList = function(value) {
  return jspb.Message.setRepeatedWrapperField(this, 1, value);
};


/**
 * @param {!proto.gendocu.example.library_app.Book=} opt_value
 * @param {number=} opt_index
 * @return {!proto.gendocu.example.library_app.Book}
 */
proto.gendocu.example.library_app.ListBookResponse.prototype.addBooks = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 1, opt_value, proto.gendocu.example.library_app.Book, opt_index);
};


/**
 * Clears the list making it empty but non-null.
 * @return {!proto.gendocu.example.library_app.ListBookResponse} returns this
 */
proto.gendocu.example.library_app.ListBookResponse.prototype.clearBooksList = function() {
  return this.setBooksList([]);
};





if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * Optional fields that are not set will be set to undefined.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     net/proto2/compiler/js/internal/generator.cc#kKeyword.
 * @param {boolean=} opt_includeInstance Deprecated. whether to include the
 *     JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @return {!Object}
 */
proto.gendocu.example.library_app.Book.prototype.toObject = function(opt_includeInstance) {
  return proto.gendocu.example.library_app.Book.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Deprecated. Whether to include
 *     the JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.gendocu.example.library_app.Book} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.gendocu.example.library_app.Book.toObject = function(includeInstance, msg) {
  var f, obj = {
    isbn: jspb.Message.getFieldWithDefault(msg, 1, ""),
    title: jspb.Message.getFieldWithDefault(msg, 2, ""),
    author: (f = msg.getAuthor()) && proto.gendocu.example.library_app.Author.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.gendocu.example.library_app.Book}
 */
proto.gendocu.example.library_app.Book.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.gendocu.example.library_app.Book;
  return proto.gendocu.example.library_app.Book.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.gendocu.example.library_app.Book} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.gendocu.example.library_app.Book}
 */
proto.gendocu.example.library_app.Book.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {string} */ (reader.readString());
      msg.setIsbn(value);
      break;
    case 2:
      var value = /** @type {string} */ (reader.readString());
      msg.setTitle(value);
      break;
    case 3:
      var value = new proto.gendocu.example.library_app.Author;
      reader.readMessage(value,proto.gendocu.example.library_app.Author.deserializeBinaryFromReader);
      msg.setAuthor(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.gendocu.example.library_app.Book.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.gendocu.example.library_app.Book.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.gendocu.example.library_app.Book} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.gendocu.example.library_app.Book.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getIsbn();
  if (f.length > 0) {
    writer.writeString(
      1,
      f
    );
  }
  f = message.getTitle();
  if (f.length > 0) {
    writer.writeString(
      2,
      f
    );
  }
  f = message.getAuthor();
  if (f != null) {
    writer.writeMessage(
      3,
      f,
      proto.gendocu.example.library_app.Author.serializeBinaryToWriter
    );
  }
};


/**
 * optional string isbn = 1;
 * @return {string}
 */
proto.gendocu.example.library_app.Book.prototype.getIsbn = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 1, ""));
};


/**
 * @param {string} value
 * @return {!proto.gendocu.example.library_app.Book} returns this
 */
proto.gendocu.example.library_app.Book.prototype.setIsbn = function(value) {
  return jspb.Message.setProto3StringField(this, 1, value);
};


/**
 * optional string title = 2;
 * @return {string}
 */
proto.gendocu.example.library_app.Book.prototype.getTitle = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 2, ""));
};


/**
 * @param {string} value
 * @return {!proto.gendocu.example.library_app.Book} returns this
 */
proto.gendocu.example.library_app.Book.prototype.setTitle = function(value) {
  return jspb.Message.setProto3StringField(this, 2, value);
};


/**
 * optional Author author = 3;
 * @return {?proto.gendocu.example.library_app.Author}
 */
proto.gendocu.example.library_app.Book.prototype.getAuthor = function() {
  return /** @type{?proto.gendocu.example.library_app.Author} */ (
    jspb.Message.getWrapperField(this, proto.gendocu.example.library_app.Author, 3));
};


/**
 * @param {?proto.gendocu.example.library_app.Author|undefined} value
 * @return {!proto.gendocu.example.library_app.Book} returns this
*/
proto.gendocu.example.library_app.Book.prototype.setAuthor = function(value) {
  return jspb.Message.setWrapperField(this, 3, value);
};


/**
 * Clears the message field making it undefined.
 * @return {!proto.gendocu.example.library_app.Book} returns this
 */
proto.gendocu.example.library_app.Book.prototype.clearAuthor = function() {
  return this.setAuthor(undefined);
};


/**
 * Returns whether this field is set.
 * @return {boolean}
 */
proto.gendocu.example.library_app.Book.prototype.hasAuthor = function() {
  return jspb.Message.getField(this, 3) != null;
};





if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * Optional fields that are not set will be set to undefined.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     net/proto2/compiler/js/internal/generator.cc#kKeyword.
 * @param {boolean=} opt_includeInstance Deprecated. whether to include the
 *     JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @return {!Object}
 */
proto.gendocu.example.library_app.Author.prototype.toObject = function(opt_includeInstance) {
  return proto.gendocu.example.library_app.Author.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Deprecated. Whether to include
 *     the JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.gendocu.example.library_app.Author} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.gendocu.example.library_app.Author.toObject = function(includeInstance, msg) {
  var f, obj = {
    firstName: jspb.Message.getFieldWithDefault(msg, 1, ""),
    lastName: jspb.Message.getFieldWithDefault(msg, 2, "")
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.gendocu.example.library_app.Author}
 */
proto.gendocu.example.library_app.Author.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.gendocu.example.library_app.Author;
  return proto.gendocu.example.library_app.Author.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.gendocu.example.library_app.Author} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.gendocu.example.library_app.Author}
 */
proto.gendocu.example.library_app.Author.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {string} */ (reader.readString());
      msg.setFirstName(value);
      break;
    case 2:
      var value = /** @type {string} */ (reader.readString());
      msg.setLastName(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.gendocu.example.library_app.Author.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.gendocu.example.library_app.Author.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.gendocu.example.library_app.Author} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.gendocu.example.library_app.Author.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getFirstName();
  if (f.length > 0) {
    writer.writeString(
      1,
      f
    );
  }
  f = message.getLastName();
  if (f.length > 0) {
    writer.writeString(
      2,
      f
    );
  }
};


/**
 * optional string first_name = 1;
 * @return {string}
 */
proto.gendocu.example.library_app.Author.prototype.getFirstName = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 1, ""));
};


/**
 * @param {string} value
 * @return {!proto.gendocu.example.library_app.Author} returns this
 */
proto.gendocu.example.library_app.Author.prototype.setFirstName = function(value) {
  return jspb.Message.setProto3StringField(this, 1, value);
};


/**
 * optional string last_name = 2;
 * @return {string}
 */
proto.gendocu.example.library_app.Author.prototype.getLastName = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 2, ""));
};


/**
 * @param {string} value
 * @return {!proto.gendocu.example.library_app.Author} returns this
 */
proto.gendocu.example.library_app.Author.prototype.setLastName = function(value) {
  return jspb.Message.setProto3StringField(this, 2, value);
};


goog.object.extend(exports, proto.gendocu.example.library_app);