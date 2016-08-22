#Generated file

SE_DEBUG_NAME = "SeDebugPrivilege"
from windows.generated_def.windef import *
SYMOPT_CASE_INSENSITIVE = Flag("SYMOPT_CASE_INSENSITIVE", 0x00000001)
SYMOPT_UNDNAME = Flag("SYMOPT_UNDNAME", 0x00000002)
SYMOPT_DEFERRED_LOADS = Flag("SYMOPT_DEFERRED_LOADS", 0x00000004)
SYMOPT_LOAD_LINES = Flag("SYMOPT_LOAD_LINES", 0x00000010)
SYMOPT_OMAP_FIND_NEAREST = Flag("SYMOPT_OMAP_FIND_NEAREST", 0x00000020)
SYMOPT_NO_UNQUALIFIED_LOADS = Flag("SYMOPT_NO_UNQUALIFIED_LOADS", 0x00000100)
SYMOPT_FAIL_CRITICAL_ERRORS = Flag("SYMOPT_FAIL_CRITICAL_ERRORS", 0x00000200)
SYMOPT_AUTO_PUBLICS = Flag("SYMOPT_AUTO_PUBLICS", 0x00010000)
SYMOPT_NO_IMAGE_SEARCH = Flag("SYMOPT_NO_IMAGE_SEARCH", 0x00020000)
DEBUG_ATTACH_KERNEL_CONNECTION = Flag("DEBUG_ATTACH_KERNEL_CONNECTION", 0x00000000)
DEBUG_ATTACH_LOCAL_KERNEL = Flag("DEBUG_ATTACH_LOCAL_KERNEL", 1)
DEBUG_END_PASSIVE = Flag("DEBUG_END_PASSIVE", 0)
DEBUG_END_ACTIVE_DETACH = Flag("DEBUG_END_ACTIVE_DETACH", 0x00000002)
DEBUG_DATA_KPCR_OFFSET = Flag("DEBUG_DATA_KPCR_OFFSET", 0)
DEBUG_DATA_KPRCB_OFFSET = Flag("DEBUG_DATA_KPRCB_OFFSET", 1)
DEBUG_DATA_KTHREAD_OFFSET = Flag("DEBUG_DATA_KTHREAD_OFFSET", 2)
DEBUG_DATA_BASE_TRANSLATION_VIRTUAL_OFFSET = Flag("DEBUG_DATA_BASE_TRANSLATION_VIRTUAL_OFFSET", 3)
DEBUG_DATA_PROCESSOR_IDENTIFICATION = Flag("DEBUG_DATA_PROCESSOR_IDENTIFICATION", 4)
DEBUG_DATA_PROCESSOR_SPEED = Flag("DEBUG_DATA_PROCESSOR_SPEED", 5)
UserMode = Flag("UserMode", 1)
MmNonCached = Flag("MmNonCached", 0)
NormalPagePriority = Flag("NormalPagePriority", 16)
DEBUG_INTERRUPT_ACTIVE = Flag("DEBUG_INTERRUPT_ACTIVE", 0)
DEBUG_END_ACTIVE_DETACH = Flag("DEBUG_END_ACTIVE_DETACH", 0x00000002)
DEBUG_BREAKPOINT_CODE = Flag("DEBUG_BREAKPOINT_CODE", 0)
DEBUG_BREAKPOINT_DATA = Flag("DEBUG_BREAKPOINT_DATA", 1)
DEBUG_BREAKPOINT_TIME = Flag("DEBUG_BREAKPOINT_TIME", 2)
DEBUG_BREAKPOINT_GO_ONLY = Flag("DEBUG_BREAKPOINT_GO_ONLY", 0x00000001)
DEBUG_BREAKPOINT_DEFERRED = Flag("DEBUG_BREAKPOINT_DEFERRED", 0x00000002)
DEBUG_BREAKPOINT_ENABLED = Flag("DEBUG_BREAKPOINT_ENABLED", 0x00000004)
DEBUG_BREAKPOINT_ADDER_ONLY = Flag("DEBUG_BREAKPOINT_ADDER_ONLY", 0x00000008)
DEBUG_BREAKPOINT_ONE_SHOT = Flag("DEBUG_BREAKPOINT_ONE_SHOT", 0x00000010)
DEBUG_BREAK_READ = Flag("DEBUG_BREAK_READ", 0x00000001)
DEBUG_BREAK_WRITE = Flag("DEBUG_BREAK_WRITE", 0x00000002)
DEBUG_BREAK_EXECUTE = Flag("DEBUG_BREAK_EXECUTE", 0x00000004)
DEBUG_BREAK_IO = Flag("DEBUG_BREAK_IO", 0x00000008)
DEBUG_ANY_ID = Flag("DEBUG_ANY_ID", 0xffffffff)
DEBUG_VALUE_INVALID = Flag("DEBUG_VALUE_INVALID", 0)
DEBUG_VALUE_INT8 = Flag("DEBUG_VALUE_INT8", 1)
DEBUG_VALUE_INT16 = Flag("DEBUG_VALUE_INT16", 2)
DEBUG_VALUE_INT32 = Flag("DEBUG_VALUE_INT32", 3)
DEBUG_VALUE_INT64 = Flag("DEBUG_VALUE_INT64", 4)
DEBUG_VALUE_FLOAT32 = Flag("DEBUG_VALUE_FLOAT32", 5)
DEBUG_VALUE_FLOAT64 = Flag("DEBUG_VALUE_FLOAT64", 6)
DEBUG_VALUE_FLOAT80 = Flag("DEBUG_VALUE_FLOAT80", 7)
DEBUG_VALUE_FLOAT82 = Flag("DEBUG_VALUE_FLOAT82", 8)
DEBUG_VALUE_FLOAT128 = Flag("DEBUG_VALUE_FLOAT128", 9)
DEBUG_VALUE_VECTOR64 = Flag("DEBUG_VALUE_VECTOR64", 10)
DEBUG_VALUE_VECTOR128 = Flag("DEBUG_VALUE_VECTOR128", 11)
DEBUG_STATUS_NO_CHANGE = Flag("DEBUG_STATUS_NO_CHANGE", 0)
DEBUG_STATUS_GO = Flag("DEBUG_STATUS_GO", 1)
DEBUG_STATUS_GO_HANDLED = Flag("DEBUG_STATUS_GO_HANDLED", 2)
DEBUG_STATUS_GO_NOT_HANDLED = Flag("DEBUG_STATUS_GO_NOT_HANDLED", 3)
DEBUG_STATUS_STEP_OVER = Flag("DEBUG_STATUS_STEP_OVER", 4)
DEBUG_STATUS_STEP_INTO = Flag("DEBUG_STATUS_STEP_INTO", 5)
DEBUG_STATUS_BREAK = Flag("DEBUG_STATUS_BREAK", 6)
DEBUG_STATUS_NO_DEBUGGEE = Flag("DEBUG_STATUS_NO_DEBUGGEE", 7)
DEBUG_STATUS_STEP_BRANCH = Flag("DEBUG_STATUS_STEP_BRANCH", 8)
DEBUG_STATUS_IGNORE_EVENT = Flag("DEBUG_STATUS_IGNORE_EVENT", 9)
DEBUG_STATUS_RESTART_REQUESTED = Flag("DEBUG_STATUS_RESTART_REQUESTED", 10)
DEBUG_STATUS_REVERSE_GO = Flag("DEBUG_STATUS_REVERSE_GO", 11)
DEBUG_STATUS_REVERSE_STEP_BRANCH = Flag("DEBUG_STATUS_REVERSE_STEP_BRANCH", 12)
DEBUG_STATUS_REVERSE_STEP_OVER = Flag("DEBUG_STATUS_REVERSE_STEP_OVER", 13)
DEBUG_STATUS_REVERSE_STEP_INTO = Flag("DEBUG_STATUS_REVERSE_STEP_INTO", 14)
DEBUG_EVENT_BREAKPOINT = Flag("DEBUG_EVENT_BREAKPOINT", 0x00000001)
DEBUG_EVENT_EXCEPTION = Flag("DEBUG_EVENT_EXCEPTION", 0x00000002)
DEBUG_EVENT_CREATE_THREAD = Flag("DEBUG_EVENT_CREATE_THREAD", 0x00000004)
DEBUG_EVENT_EXIT_THREAD = Flag("DEBUG_EVENT_EXIT_THREAD", 0x00000008)
DEBUG_EVENT_CREATE_PROCESS = Flag("DEBUG_EVENT_CREATE_PROCESS", 0x00000010)
DEBUG_EVENT_EXIT_PROCESS = Flag("DEBUG_EVENT_EXIT_PROCESS", 0x00000020)
DEBUG_EVENT_LOAD_MODULE = Flag("DEBUG_EVENT_LOAD_MODULE", 0x00000040)
DEBUG_EVENT_UNLOAD_MODULE = Flag("DEBUG_EVENT_UNLOAD_MODULE", 0x00000080)
DEBUG_EVENT_SYSTEM_ERROR = Flag("DEBUG_EVENT_SYSTEM_ERROR", 0x00000100)
DEBUG_EVENT_SESSION_STATUS = Flag("DEBUG_EVENT_SESSION_STATUS", 0x00000200)
DEBUG_EVENT_CHANGE_DEBUGGEE_STATE = Flag("DEBUG_EVENT_CHANGE_DEBUGGEE_STATE", 0x00000400)
DEBUG_EVENT_CHANGE_ENGINE_STATE = Flag("DEBUG_EVENT_CHANGE_ENGINE_STATE", 0x00000800)
DEBUG_EVENT_CHANGE_SYMBOL_STATE = Flag("DEBUG_EVENT_CHANGE_SYMBOL_STATE", 0x00001000)
DEBUG_EXECUTE_DEFAULT = Flag("DEBUG_EXECUTE_DEFAULT", 0x00000000)
DEBUG_EXECUTE_ECHO = Flag("DEBUG_EXECUTE_ECHO", 0x00000001)
DEBUG_EXECUTE_NOT_LOGGED = Flag("DEBUG_EXECUTE_NOT_LOGGED", 0x00000002)
DEBUG_EXECUTE_NO_REPEAT = Flag("DEBUG_EXECUTE_NO_REPEAT", 0x00000004)