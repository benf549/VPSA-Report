#include "Python.h"
extern PyObject* PyInit__abc(void);
extern PyObject* PyInit__ast(void);
extern PyObject* PyInit__asyncio(void);
extern PyObject* PyInit__bisect(void);
extern PyObject* PyInit__blake2(void);
extern PyObject* PyInit__bz2(void);
extern PyObject* PyInit__codecs(void);
extern PyObject* PyInit__codecs_cn(void);
extern PyObject* PyInit__codecs_hk(void);
extern PyObject* PyInit__codecs_iso2022(void);
extern PyObject* PyInit__codecs_jp(void);
extern PyObject* PyInit__codecs_kr(void);
extern PyObject* PyInit__codecs_tw(void);
extern PyObject* PyInit__collections(void);
extern PyObject* PyInit__contextvars(void);
extern PyObject* PyInit__csv(void);
extern PyObject* PyInit__ctypes(void);
extern PyObject* PyInit__datetime(void);
extern PyObject* PyInit__decimal(void);
extern PyObject* PyInit__elementtree(void);
extern PyObject* PyInit__functools(void);
extern PyObject* PyInit__hashlib(void);
extern PyObject* PyInit__heapq(void);
extern PyObject* PyInit__imp(void);
extern PyObject* PyInit__io(void);
extern PyObject* PyInit__json(void);
extern PyObject* PyInit__locale(void);
extern PyObject* PyInit__lsprof(void);
extern PyObject* PyInit__lzma(void);
extern PyObject* PyInit__md5(void);
extern PyObject* PyInit__msi(void);
extern PyObject* PyInit__multibytecodec(void);
extern PyObject* PyInit__multiprocessing(void);
extern PyObject* PyInit__opcode(void);
extern PyObject* PyInit__operator(void);
extern PyObject* PyInit__overlapped(void);
extern PyObject* PyInit__pickle(void);
extern PyObject* PyInit__queue(void);
extern PyObject* PyInit__random(void);
extern PyObject* PyInit__sha1(void);
extern PyObject* PyInit__sha256(void);
extern PyObject* PyInit__sha3(void);
extern PyObject* PyInit__sha512(void);
extern PyObject* PyInit__signal(void);
extern PyObject* PyInit__socket(void);
extern PyObject* PyInit__sqlite3(void);
extern PyObject* PyInit__sre(void);
extern PyObject* PyInit__ssl(void);
extern PyObject* PyInit__stat(void);
extern PyObject* PyInit__string(void);
extern PyObject* PyInit__struct(void);
extern PyObject* PyInit__symtable(void);
extern PyObject* PyInit__thread(void);
extern PyObject* PyInit__tracemalloc(void);
extern PyObject* _PyWarnings_Init(void);
extern PyObject* PyInit__weakref(void);
extern PyObject* PyInit__winapi(void);
extern PyObject* PyInit_array(void);
extern PyObject* PyInit_atexit(void);
extern PyObject* PyInit_audioop(void);
extern PyObject* PyInit_binascii(void);
extern PyObject* PyInit_cmath(void);
extern PyObject* PyInit_errno(void);
extern PyObject* PyInit_faulthandler(void);
extern PyObject* PyInit_gc(void);
extern PyObject* PyInit_itertools(void);
extern PyObject* PyMarshal_Init(void);
extern PyObject* PyInit_math(void);
extern PyObject* PyInit_mmap(void);
extern PyObject* PyInit_msvcrt(void);
extern PyObject* PyInit_nt(void);
extern PyObject* PyInit_parser(void);
extern PyObject* PyInit_pyexpat(void);
extern PyObject* PyInit_select(void);
extern PyObject* PyInit_time(void);
extern PyObject* PyInit_unicodedata(void);
extern PyObject* PyInit_winreg(void);
extern PyObject* PyInit_winsound(void);
extern PyObject* PyInit_xxsubtype(void);
extern PyObject* PyInit_zipimport(void);
extern PyObject* PyInit_zlib(void);
struct _inittab _PyImport_Inittab[] = {
{"_abc", PyInit__abc},
{"_ast", PyInit__ast},
{"_asyncio", PyInit__asyncio},
{"_bisect", PyInit__bisect},
{"_blake2", PyInit__blake2},
{"_bz2", PyInit__bz2},
{"_codecs", PyInit__codecs},
{"_codecs_cn", PyInit__codecs_cn},
{"_codecs_hk", PyInit__codecs_hk},
{"_codecs_iso2022", PyInit__codecs_iso2022},
{"_codecs_jp", PyInit__codecs_jp},
{"_codecs_kr", PyInit__codecs_kr},
{"_codecs_tw", PyInit__codecs_tw},
{"_collections", PyInit__collections},
{"_contextvars", PyInit__contextvars},
{"_csv", PyInit__csv},
{"_ctypes", PyInit__ctypes},
{"_datetime", PyInit__datetime},
{"_decimal", PyInit__decimal},
{"_elementtree", PyInit__elementtree},
{"_functools", PyInit__functools},
{"_hashlib", PyInit__hashlib},
{"_heapq", PyInit__heapq},
{"_imp", PyInit__imp},
{"_io", PyInit__io},
{"_json", PyInit__json},
{"_locale", PyInit__locale},
{"_lsprof", PyInit__lsprof},
{"_lzma", PyInit__lzma},
{"_md5", PyInit__md5},
{"_msi", PyInit__msi},
{"_multibytecodec", PyInit__multibytecodec},
{"_multiprocessing", PyInit__multiprocessing},
{"_opcode", PyInit__opcode},
{"_operator", PyInit__operator},
{"_overlapped", PyInit__overlapped},
{"_pickle", PyInit__pickle},
{"_queue", PyInit__queue},
{"_random", PyInit__random},
{"_sha1", PyInit__sha1},
{"_sha256", PyInit__sha256},
{"_sha3", PyInit__sha3},
{"_sha512", PyInit__sha512},
{"_signal", PyInit__signal},
{"_socket", PyInit__socket},
{"_sqlite3", PyInit__sqlite3},
{"_sre", PyInit__sre},
{"_ssl", PyInit__ssl},
{"_stat", PyInit__stat},
{"_string", PyInit__string},
{"_struct", PyInit__struct},
{"_symtable", PyInit__symtable},
{"_thread", PyInit__thread},
{"_tracemalloc", PyInit__tracemalloc},
{"_warnings", _PyWarnings_Init},
{"_weakref", PyInit__weakref},
{"_winapi", PyInit__winapi},
{"array", PyInit_array},
{"atexit", PyInit_atexit},
{"audioop", PyInit_audioop},
{"binascii", PyInit_binascii},
{"cmath", PyInit_cmath},
{"errno", PyInit_errno},
{"faulthandler", PyInit_faulthandler},
{"gc", PyInit_gc},
{"itertools", PyInit_itertools},
{"marshal", PyMarshal_Init},
{"math", PyInit_math},
{"mmap", PyInit_mmap},
{"msvcrt", PyInit_msvcrt},
{"nt", PyInit_nt},
{"parser", PyInit_parser},
{"pyexpat", PyInit_pyexpat},
{"select", PyInit_select},
{"time", PyInit_time},
{"unicodedata", PyInit_unicodedata},
{"winreg", PyInit_winreg},
{"winsound", PyInit_winsound},
{"xxsubtype", PyInit_xxsubtype},
{"zipimport", PyInit_zipimport},
{"zlib", PyInit_zlib},
{0, 0}
};