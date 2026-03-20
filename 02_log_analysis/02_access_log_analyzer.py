# Project: Forensic investigation for Cross-Departmental Resource Access
# Author: Douglas Akwasi Kwarteng

# Import Libraries
import pandas as pd

def norm(text):
    return str(text).strip().lower()

def analyze_logs(datalog_path, emp_details_path, dept_resource_path, out_path):
    # Load the data
    datalog = pd.read_csv(datalog_path)
    emp_details = pd.read_csv(emp_details_path)
    dept_resource = pd.read_csv(dept_resource_path)

    # Clean column names
    datalog.columns = [c.strip() for c in datalog.columns]
    emp_details.columns = [c.strip() for c in emp_details.columns]
    dept_resource.columns = [c.strip() for c in dept_resource.columns]

    # Normalize fields for matching
    datalog["EmployeeID"] = datalog["EmployeeID"].astype(int)
    datalog["res_norm"] = datalog["ResourceID"].map(norm)
    emp_details["EmployeeID"] = emp_details["EmployeeID"].astype(int)
    emp_details["dept_norm"] = emp_details["Department"].map(norm)
    dept_resource["res_norm"] = dept_resource["ResourceID"].map(norm)
    dept_resource["dept_norm"] = dept_resource["Department"].map(norm)

    # Build lookups
    res_dept_orig_map = dict(zip(dept_resource["res_norm"], dept_resource["Department"]))
    res_dept_norm_map = dict(zip(dept_resource["res_norm"], dept_resource["dept_norm"]))

    # Merge employee info
    datalog = datalog.merge(emp_details[["EmployeeID", "Name", "Department", "dept_norm"]], on="EmployeeID", how="left")

    # Map resource departments
    datalog["ResourceDept"] = datalog["res_norm"].map(res_dept_orig_map)
    datalog["ResourceDeptNorm"] = datalog["res_norm"].map(res_dept_norm_map)

    # Flag cross-department access
    datalog["is_cross_dept"] = (datalog["dept_norm"].notna() & 
                                datalog["ResourceDeptNorm"].notna() & 
                                (datalog["dept_norm"] != datalog["ResourceDeptNorm"]))

    # Filter and format output
    cross = datalog[datalog["is_cross_dept"]].copy()
    cross = cross.rename(columns={
        "Name": "Emp_name",
        "Department": "Emp_department",
        "ResourceID": "Accessed_resource",
        "ResourceDept": "Accessed_resource_dept",
        "Datetime": "Date_time",
        "Result": "Results"
    })

    output_cols = ["Emp_name", "Emp_department", "Accessed_resource", "Accessed_resource_dept", "Date_time", "Results"]
    cross = cross[output_cols]
    
    cross.to_csv(out_path, index=False)
    print(f"Analysis complete. Results saved to {out_path}")

if __name__ == "__main__":
    # Example usage
    # analyze_logs("datalog.csv", "employees.csv", "resources.csv", "alerts.csv")
    pass